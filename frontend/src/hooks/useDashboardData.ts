import { useCallback, useEffect, useMemo, useRef, useState } from "react";

import { API_BASE_URL } from "@/config";
import {
  getHealth,
  getItemDetail,
  listCourses,
  listItems,
  listModules,
  queueSummary,
  queueTranscript,
  refreshCourses,
  refreshModuleItems,
  refreshModules,
} from "@/lib/api";
import type { Course, Item, ItemDetail, ItemStatus, Module } from "@/types";

export interface DashboardFilters {
  search: string;
  provider: string;
  status: ItemStatus[];
}

export type DashboardAction = "transcript" | "summary" | null;

export interface ActionMessage {
  type: "success" | "error";
  text: string;
}

export interface DashboardState {
  readonly apiBaseUrl: string;
  readonly healthStatus: string | null;
  readonly healthError: string | null;
  readonly actionMessage: ActionMessage | null;
  readonly courses: Course[];
  readonly loadingCourses: boolean;
  readonly coursesError: string | null;
  readonly selectedCourseId: number | null;
  readonly refreshingCourses: boolean;
  readonly modules: Module[];
  readonly loadingModules: boolean;
  readonly modulesError: string | null;
  readonly selectedModuleId: number | null;
  readonly refreshingModules: boolean;
  readonly items: Item[];
  readonly loadingItems: boolean;
  readonly itemsError: string | null;
  readonly selectedItemId: number | null;
  readonly filters: DashboardFilters;
  readonly providerOptions: string[];
  readonly itemDetail: ItemDetail | null;
  readonly loadingDetail: boolean;
  readonly detailError: string | null;
  readonly actionBusy: DashboardAction;
  selectCourse: (courseId: number) => void;
  selectModule: (moduleId: number) => void;
  selectItem: (itemId: number) => void;
  refreshCourses: () => Promise<void>;
  refreshModules: () => Promise<void>;
  setSearch: (value: string) => void;
  setProvider: (value: string) => void;
  toggleStatus: (value: ItemStatus) => void;
  resetFilters: () => void;
  queueTranscript: () => Promise<void>;
  queueSummary: () => Promise<void>;
}

export function useDashboardData(): DashboardState {
  const [healthStatus, setHealthStatus] = useState<string | null>(null);
  const [healthError, setHealthError] = useState<string | null>(null);

  const [courses, setCourses] = useState<Course[]>([]);
  const [loadingCourses, setLoadingCourses] = useState(false);
  const [coursesError, setCoursesError] = useState<string | null>(null);
  const [selectedCourseId, setSelectedCourseId] = useState<number | null>(null);

  const [modules, setModules] = useState<Module[]>([]);
  const [loadingModules, setLoadingModules] = useState(false);
  const [modulesError, setModulesError] = useState<string | null>(null);
  const [selectedModuleId, setSelectedModuleId] = useState<number | null>(null);

  const [items, setItems] = useState<Item[]>([]);
  const [loadingItems, setLoadingItems] = useState(false);
  const [itemsError, setItemsError] = useState<string | null>(null);
  const [selectedItemId, setSelectedItemId] = useState<number | null>(null);

  const [itemDetail, setItemDetail] = useState<ItemDetail | null>(null);
  const [loadingDetail, setLoadingDetail] = useState(false);
  const [detailError, setDetailError] = useState<string | null>(null);

  const [filters, setFilters] = useState<DashboardFilters>({
    search: "",
    provider: "",
    status: [],
  });

  const [refreshingCourses, setRefreshingCourses] = useState(false);
  const [refreshingModules, setRefreshingModules] = useState(false);
  const [actionMessage, setActionMessage] = useState<ActionMessage | null>(null);
  const [actionBusy, setActionBusy] = useState<DashboardAction>(null);

  const filtersRef = useRef(filters);
  const selectedModuleIdRef = useRef<number | null>(selectedModuleId);
  const selectedItemIdRef = useRef<number | null>(selectedItemId);
  const lastModuleSyncedRef = useRef<number | null>(null);

  useEffect(() => {
    const loadHealth = async () => {
      try {
        const response = await getHealth();
        setHealthStatus(response.status);
        setHealthError(null);
      } catch (error) {
        setHealthStatus(null);
        setHealthError(
          error instanceof Error ? error.message : "Unable to reach API",
        );
      }
    };
    void loadHealth();
  }, []);

  const loadCourses = useCallback(async () => {
    setLoadingCourses(true);
    setCoursesError(null);
    try {
      const data = await listCourses();
      setCourses(data);
      setSelectedCourseId((previous) =>
        previous && data.some((course) => course.id === previous) ? previous : null,
      );
    } catch (error) {
      setCoursesError(error instanceof Error ? error.message : "Failed to load courses.");
      setCourses([]);
      setSelectedCourseId(null);
    } finally {
      setLoadingCourses(false);
    }
  }, []);

  useEffect(() => {
    void loadCourses();
  }, [loadCourses]);

  const loadModules = useCallback(
    async (courseId: number | null): Promise<number | null> => {
      if (!courseId) {
        setModules([]);
        setSelectedModuleId(null);
        return null;
      }
      setLoadingModules(true);
      setModulesError(null);
      let nextModuleId: number | null = null;
      try {
        const data = await listModules(courseId);
        setModules(data);
        setSelectedModuleId((previous) => {
          const next = previous && data.some((module) => module.id === previous) ? previous : null;
          nextModuleId = next;
          return next;
        });
      } catch (error) {
        setModulesError(error instanceof Error ? error.message : "Failed to load modules.");
        setModules([]);
        setSelectedModuleId(null);
        nextModuleId = null;
      } finally {
        setLoadingModules(false);
      }
      return nextModuleId;
    },
    [],
  );

  const syncModules = useCallback(
    async (
      courseId: number,
      options: { includeItems?: boolean; showToast?: boolean } = {},
    ) => {
      let errorMessage: string | null = null;
      setRefreshingModules(true);
      try {
        await refreshModules(courseId, { includeItems: options.includeItems ?? true });
        if (options.showToast) {
          setActionMessage({ type: "success", text: "Modules refreshed." });
        }
      } catch (error) {
        errorMessage = error instanceof Error ? error.message : "Failed to refresh modules.";
        if (options.showToast) {
          setActionMessage({ type: "error", text: errorMessage });
        }
      } finally {
        setRefreshingModules(false);
        await loadModules(courseId);
        if (!options.showToast && errorMessage) {
          setModulesError(errorMessage);
        }
      }
    },
    [loadModules, refreshModules],
  );

  const loadItems = useCallback(
    async (moduleId: number | null, nextFilters: DashboardFilters) => {
      if (!moduleId) {
        setItems([]);
        setSelectedItemId(null);
        return;
      }
      setLoadingItems(true);
      setItemsError(null);
      try {
        const data = await listItems({
          moduleId: moduleId ?? undefined,
          status: nextFilters.status.length ? nextFilters.status : undefined,
          provider: nextFilters.provider || undefined,
          search: nextFilters.search || undefined,
        });
        setItems(data);
        setSelectedItemId((previous) => {
          if (previous && data.some((item) => item.id === previous)) {
            return previous;
          }
          return data.length ? data[0].id : null;
        });
      } catch (error) {
        setItemsError(error instanceof Error ? error.message : "Failed to load items.");
        setItems([]);
        setSelectedItemId(null);
      } finally {
        setLoadingItems(false);
      }
    },
    [],
  );

  const syncItemsForModule = useCallback(
    async (
      moduleId: number,
      nextFilters: DashboardFilters,
      options: { showToast?: boolean; forceRefresh?: boolean } = {},
    ) => {
      let errorMessage: string | null = null;
      if (options.forceRefresh || lastModuleSyncedRef.current !== moduleId) {
        try {
          await refreshModuleItems(moduleId);
          lastModuleSyncedRef.current = moduleId;
          if (options.showToast) {
            setActionMessage({ type: "success", text: "Items refreshed." });
          }
        } catch (error) {
          errorMessage =
            error instanceof Error ? error.message : "Failed to refresh module items.";
          if (options.showToast) {
            setActionMessage({ type: "error", text: errorMessage });
          }
        }
      }
      await loadItems(moduleId, nextFilters);
      if (!options.showToast && errorMessage) {
        setItemsError(errorMessage);
      }
    },
    [loadItems, refreshModuleItems],
  );

  const loadItemDetail = useCallback(async (itemId: number | null) => {
    if (!itemId) {
      setItemDetail(null);
      return;
    }
    setLoadingDetail(true);
    setDetailError(null);
    try {
      const data = await getItemDetail(itemId);
      setItemDetail(data);
    } catch (error) {
      setDetailError(
        error instanceof Error ? error.message : "Failed to load item details.",
      );
      setItemDetail(null);
    } finally {
      setLoadingDetail(false);
    }
  }, []);

  useEffect(() => {
    void loadItemDetail(selectedItemId);
  }, [selectedItemId, loadItemDetail]);

  useEffect(() => {
    if (!actionMessage) {
      return;
    }
    const timeout = window.setTimeout(() => setActionMessage(null), 4000);
    return () => window.clearTimeout(timeout);
  }, [actionMessage]);

  useEffect(() => {
    filtersRef.current = filters;
  }, [filters]);

  useEffect(() => {
    selectedModuleIdRef.current = selectedModuleId;
  }, [selectedModuleId]);

  useEffect(() => {
    selectedItemIdRef.current = selectedItemId;
  }, [selectedItemId]);

  const providerOptions = useMemo(() => {
    const providers = new Set<string>();
    for (const item of items) {
      if (item.provider) {
        providers.add(item.provider);
      }
    }
    return Array.from(providers).sort((a, b) => a.localeCompare(b));
  }, [items]);

  const handleRefreshCourses = useCallback(async () => {
    setRefreshingCourses(true);
    try {
      await refreshCourses();
      await loadCourses();
      setActionMessage({ type: "success", text: "Courses refreshed." });
    } catch (error) {
      setActionMessage({
        type: "error",
        text: error instanceof Error ? error.message : "Failed to refresh courses.",
      });
    } finally {
      setRefreshingCourses(false);
    }
  }, [loadCourses]);

  const handleRefreshModules = useCallback(async () => {
    if (!selectedCourseId) {
      return;
    }
    await syncModules(selectedCourseId, { includeItems: false, showToast: true });
    const currentModuleId = selectedModuleIdRef.current;
    if (currentModuleId) {
      await syncItemsForModule(currentModuleId, filtersRef.current, {
        forceRefresh: true,
      });
    }
  }, [selectedCourseId, syncModules, syncItemsForModule]);

  const handleQueueTranscript = useCallback(async () => {
    if (!selectedItemId) {
      return;
    }
    setActionBusy("transcript");
    try {
      await queueTranscript(selectedItemId);
      if (selectedModuleId) {
        await loadItems(selectedModuleId, filters);
      }
      await loadItemDetail(selectedItemId);
      setActionMessage({ type: "success", text: "Transcript job queued." });
    } catch (error) {
      setActionMessage({
        type: "error",
        text: error instanceof Error ? error.message : "Failed to queue transcript.",
      });
    } finally {
      setActionBusy((current) => (current === "transcript" ? null : current));
    }
  }, [filters, loadItemDetail, loadItems, selectedItemId, selectedModuleId]);

  const handleQueueSummary = useCallback(async () => {
    if (!selectedItemId) {
      return;
    }
    setActionBusy("summary");
    try {
      await queueSummary(selectedItemId);
      if (selectedModuleId) {
        await loadItems(selectedModuleId, filters);
      }
      await loadItemDetail(selectedItemId);
      setActionMessage({ type: "success", text: "Summary job queued." });
    } catch (error) {
      setActionMessage({
        type: "error",
        text: error instanceof Error ? error.message : "Failed to queue summary.",
      });
    } finally {
      setActionBusy((current) => (current === "summary" ? null : current));
    }
  }, [filters, loadItemDetail, loadItems, selectedItemId, selectedModuleId]);

  const handleSelectCourse = useCallback((courseId: number) => {
    setSelectedCourseId(courseId);
    setSelectedModuleId(null);
    setSelectedItemId(null);
  }, []);

  const handleSelectModule = useCallback((moduleId: number) => {
    setSelectedModuleId(moduleId);
    setSelectedItemId(null);
  }, []);

  const handleSelectItem = useCallback((itemId: number) => {
    setSelectedItemId(itemId);
  }, []);

  const setSearch = useCallback((value: string) => {
    setFilters((previous) => ({ ...previous, search: value }));
  }, []);

  const setProvider = useCallback((value: string) => {
    setFilters((previous) => ({ ...previous, provider: value }));
  }, []);

  const toggleStatus = useCallback((value: ItemStatus) => {
    setFilters((previous) => {
      const exists = previous.status.includes(value);
      return {
        ...previous,
        status: exists
          ? previous.status.filter((status) => status !== value)
          : [...previous.status, value],
      };
    });
  }, []);

  const resetFilters = useCallback(() => {
    setFilters({
      search: "",
      provider: "",
      status: [],
    });
  }, []);

  const websocketUrl = useMemo(() => {
    try {
      const url = new URL(API_BASE_URL);
      url.protocol = url.protocol === "https:" ? "wss:" : "ws:";
      url.pathname = "/ws/events";
      url.search = "";
      url.hash = "";
      return url.toString();
    } catch (error) {
      console.warn("Invalid API base URL for websocket connection:", error);
      return null;
    }
  }, []);

  useEffect(() => {
    if (!websocketUrl) {
      return;
    }
    let socket: WebSocket | null = null;
    let reconnectTimer: number | undefined;
    let intentionalClose = false;

    const scheduleReconnect = () => {
      if (intentionalClose || reconnectTimer) {
        return;
      }
      reconnectTimer = window.setTimeout(() => {
        reconnectTimer = undefined;
        connect();
      }, 2000);
    };

    const connect = () => {
      socket = new WebSocket(websocketUrl);
      socket.addEventListener("message", (event) => {
        try {
          const payload = JSON.parse(event.data);
          if (payload?.type === "item.update" && payload?.item?.id) {
            const currentModuleId = selectedModuleIdRef.current;
            void loadItems(currentModuleId, filtersRef.current);
            if (selectedItemIdRef.current === payload.item.id) {
              void loadItemDetail(payload.item.id);
            }
          }
        } catch (error) {
          console.warn("Failed to parse websocket payload", error);
        }
      });
      socket.addEventListener("open", () => {
        // Reset reconnection attempts on successful open.
        if (reconnectTimer) {
          window.clearTimeout(reconnectTimer);
          reconnectTimer = undefined;
        }
      });
      socket.addEventListener("close", () => {
        if (!intentionalClose) {
          scheduleReconnect();
        }
      });
      socket.addEventListener("error", () => {
        if (!intentionalClose) {
          socket?.close();
        }
      });
    };

    connect();

    return () => {
      intentionalClose = true;
      if (reconnectTimer) {
        window.clearTimeout(reconnectTimer);
      }
      if (socket) {
        if (socket.readyState === WebSocket.OPEN) {
          socket.close();
        } else if (socket.readyState === WebSocket.CONNECTING) {
          socket.addEventListener("open", () => socket?.close(), { once: true });
        }
      }
    };
  }, [websocketUrl, loadItems, loadItemDetail]);

  useEffect(() => {
    const courseId = selectedCourseId;
    if (!courseId) {
      setModules([]);
      setSelectedModuleId(null);
      lastModuleSyncedRef.current = null;
      return;
    }
    void syncModules(courseId, { includeItems: false });
  }, [selectedCourseId, syncModules]);
  useEffect(() => {
    const moduleId = selectedModuleId;
    if (!moduleId) {
      setItems([]);
      setSelectedItemId(null);
      lastModuleSyncedRef.current = null;
      return;
    }
    void syncItemsForModule(moduleId, filters, {
      forceRefresh: lastModuleSyncedRef.current !== moduleId,
    });
  }, [selectedModuleId, filters, syncItemsForModule]);


  return {
    apiBaseUrl: API_BASE_URL,
    healthStatus,
    healthError,
    actionMessage,
    courses,
    loadingCourses,
    coursesError,
    selectedCourseId,
    refreshingCourses,
    modules,
    loadingModules,
    modulesError,
    selectedModuleId,
    refreshingModules,
    items,
    loadingItems,
    itemsError,
    selectedItemId,
    filters,
    providerOptions,
    itemDetail,
    loadingDetail,
    detailError,
    actionBusy,
    selectCourse: handleSelectCourse,
    selectModule: handleSelectModule,
    selectItem: handleSelectItem,
    refreshCourses: handleRefreshCourses,
    refreshModules: handleRefreshModules,
    setSearch,
    setProvider,
    toggleStatus,
    resetFilters,
    queueTranscript: handleQueueTranscript,
    queueSummary: handleQueueSummary,
  };
}
