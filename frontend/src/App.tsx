import { useEffect, useMemo, useState } from "react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
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
  refreshModules,
} from "@/lib/api";
import { cn } from "@/lib/utils";
import type { Course, Item, ItemDetail, ItemStatus, Module } from "@/types";

const statusInfo: Record<
  ItemStatus,
  { label: string; variant: "default" | "secondary" | "destructive" | "outline" }
> = {
  DISCOVERED: { label: "Discovered", variant: "outline" },
  TRANSCRIPT_READY: { label: "Transcript Ready", variant: "secondary" },
  SUMMARY_READY: { label: "Summary Ready", variant: "default" },
  FAILED: { label: "Failed", variant: "destructive" },
};

const statusFilters: { value: ItemStatus; label: string }[] = [
  { value: "DISCOVERED", label: "Discovered" },
  { value: "TRANSCRIPT_READY", label: "Transcript Ready" },
  { value: "SUMMARY_READY", label: "Summary Ready" },
  { value: "FAILED", label: "Failed" },
];

function formatDateTime(value?: string | null): string {
  if (!value) {
    return "Never";
  }
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    return value;
  }
  return date.toLocaleString();
}

type ActionMessage = { type: "success" | "error"; text: string };

function App() {
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

  const [filters, setFilters] = useState<{
    search: string;
    provider: string;
    status: ItemStatus[];
  }>({
    search: "",
    provider: "",
    status: [],
  });

  const [refreshingCourses, setRefreshingCourses] = useState(false);
  const [refreshingModules, setRefreshingModules] = useState(false);
  const [actionMessage, setActionMessage] = useState<ActionMessage | null>(null);
  const [actionBusy, setActionBusy] = useState<"transcript" | "summary" | null>(null);

  useEffect(() => {
    const loadHealth = async () => {
      try {
        const res = await getHealth();
        setHealthStatus(res.status);
        setHealthError(null);
      } catch (error) {
        setHealthStatus(null);
        setHealthError(error instanceof Error ? error.message : "Unable to reach API");
      }
    };
    void loadHealth();
  }, []);

  const loadCourses = async () => {
    setLoadingCourses(true);
    setCoursesError(null);
    try {
      const data = await listCourses();
      setCourses(data);
      setSelectedCourseId((prev) => {
        if (prev && data.some((course) => course.id === prev)) {
          return prev;
        }
        return data.length ? data[0].id : null;
      });
    } catch (error) {
      setCoursesError(
        error instanceof Error ? error.message : "Failed to load courses.",
      );
      setCourses([]);
      setSelectedCourseId(null);
    } finally {
      setLoadingCourses(false);
    }
  };

  useEffect(() => {
    void loadCourses();
  }, []);

  const loadModules = async (courseId: number | null): Promise<number | null> => {
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
      setSelectedModuleId((prev) => {
        const next =
          prev && data.some((module) => module.id === prev)
            ? prev
            : data.length
              ? data[0].id
              : null;
        nextModuleId = next;
        return next;
      });
    } catch (error) {
      setModulesError(
        error instanceof Error ? error.message : "Failed to load modules.",
      );
      setModules([]);
      setSelectedModuleId(null);
      nextModuleId = null;
    } finally {
      setLoadingModules(false);
    }
    return nextModuleId;
  };

  useEffect(() => {
    void loadModules(selectedCourseId);
  }, [selectedCourseId]);

  const loadItems = async (
    moduleId: number | null,
    courseId: number | null,
    nextFilters: typeof filters,
  ) => {
    if (!moduleId && !courseId) {
      setItems([]);
      setSelectedItemId(null);
      return;
    }
    setLoadingItems(true);
    setItemsError(null);
    try {
      const data = await listItems({
        moduleId: moduleId ?? undefined,
        courseId: moduleId ? undefined : courseId ?? undefined,
        status: nextFilters.status.length ? nextFilters.status : undefined,
        provider: nextFilters.provider || undefined,
        search: nextFilters.search || undefined,
      });
      setItems(data);
      setSelectedItemId((prev) => {
        if (prev && data.some((item) => item.id === prev)) {
          return prev;
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
  };

  useEffect(() => {
    void loadItems(selectedModuleId, selectedCourseId, filters);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedModuleId, selectedCourseId, filters]);

  const loadItemDetail = async (itemId: number | null) => {
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
  };

  useEffect(() => {
    void loadItemDetail(selectedItemId);
  }, [selectedItemId]);

  useEffect(() => {
    if (!actionMessage) {
      return;
    }
    const timeout = window.setTimeout(() => setActionMessage(null), 4000);
    return () => window.clearTimeout(timeout);
  }, [actionMessage]);

  const providerOptions = useMemo(() => {
    const providers = new Set<string>();
    for (const item of items) {
      if (item.provider) {
        providers.add(item.provider);
      }
    }
    return Array.from(providers).sort((a, b) => a.localeCompare(b));
  }, [items]);

  const handleRefreshCourses = async () => {
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
  };

  const handleRefreshModules = async () => {
    if (!selectedCourseId) {
      return;
    }
    setRefreshingModules(true);
    try {
      await refreshModules(selectedCourseId);
      const nextModuleId = await loadModules(selectedCourseId);
      await loadItems(nextModuleId, selectedCourseId, filters);
      setActionMessage({ type: "success", text: "Modules refreshed." });
    } catch (error) {
      setActionMessage({
        type: "error",
        text: error instanceof Error ? error.message : "Failed to refresh modules.",
      });
    } finally {
      setRefreshingModules(false);
    }
  };

  const handleQueueTranscript = async () => {
    if (!selectedItemId) {
      return;
    }
    setActionBusy("transcript");
    try {
      await queueTranscript(selectedItemId);
      await loadItems(selectedModuleId, selectedCourseId, filters);
      await loadItemDetail(selectedItemId);
      setActionMessage({
        type: "success",
        text: "Transcript job queued.",
      });
    } catch (error) {
      setActionMessage({
        type: "error",
        text: error instanceof Error ? error.message : "Failed to queue transcript.",
      });
    } finally {
      setActionBusy((current) => (current === "transcript" ? null : current));
    }
  };

  const handleQueueSummary = async () => {
    if (!selectedItemId) {
      return;
    }
    setActionBusy("summary");
    try {
      await queueSummary(selectedItemId);
      await loadItems(selectedModuleId, selectedCourseId, filters);
      await loadItemDetail(selectedItemId);
      setActionMessage({
        type: "success",
        text: "Summary job queued.",
      });
    } catch (error) {
      setActionMessage({
        type: "error",
        text: error instanceof Error ? error.message : "Failed to queue summary.",
      });
    } finally {
      setActionBusy((current) => (current === "summary" ? null : current));
    }
  };

  const selectedCourse = courses.find((course) => course.id === selectedCourseId) ?? null;
  const selectedModule = modules.find((module) => module.id === selectedModuleId) ?? null;

  const selectedStatusInfo = itemDetail ? statusInfo[itemDetail.status] : null;

  return (
    <div className="min-h-screen bg-background text-foreground">
      <header className="border-b bg-card">
        <div className="container flex flex-col gap-2 py-6 md:flex-row md:items-center md:justify-between">
          <div>
            <h1 className="text-2xl font-semibold tracking-tight">
              Canvas Summarization Dashboard
            </h1>
            <p className="text-sm text-muted-foreground">
              Connected to <span className="font-mono">{API_BASE_URL}</span>
            </p>
          </div>
          <div className="flex flex-wrap items-center gap-2 text-sm text-muted-foreground">
            <span>
              Health:{" "}
              {healthError ? (
                <span className="text-destructive">{healthError}</span>
              ) : healthStatus ? (
                <span className="text-emerald-600 dark:text-emerald-400">{healthStatus}</span>
              ) : (
                "Checking…"
              )}
            </span>
            {actionMessage && (
              <Badge
                variant={actionMessage.type === "success" ? "secondary" : "destructive"}
                className="font-normal"
              >
                {actionMessage.text}
              </Badge>
            )}
          </div>
        </div>
      </header>
      <main className="container grid gap-6 py-6">
        <section className="grid gap-4 lg:grid-cols-[280px_320px_1fr]">
          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0">
              <div>
                <CardTitle className="text-lg">Courses</CardTitle>
                <CardDescription>Refresh courses, then pick one to explore.</CardDescription>
              </div>
              <Button
                size="sm"
                variant="outline"
                onClick={handleRefreshCourses}
                disabled={refreshingCourses}
              >
                {refreshingCourses ? "Refreshing…" : "Refresh"}
              </Button>
            </CardHeader>
            <CardContent>
              {coursesError ? (
                <p className="text-sm text-destructive">{coursesError}</p>
              ) : loadingCourses ? (
                <p className="text-sm text-muted-foreground">Loading courses…</p>
              ) : courses.length === 0 ? (
                <p className="text-sm text-muted-foreground">
                  No courses yet. Click refresh after configuring Canvas credentials.
                </p>
              ) : (
                <ScrollArea className="h-[420px]">
                  <div className="space-y-2">
                    {courses.map((course) => (
                      <button
                        key={course.id}
                        type="button"
                        onClick={() => setSelectedCourseId(course.id)}
                        className={cn(
                          "w-full rounded-md border px-3 py-2 text-left transition-colors hover:bg-accent",
                          selectedCourseId === course.id
                            ? "border-primary bg-accent"
                            : "border-transparent",
                        )}
                      >
                        <div className="font-medium">{course.name}</div>
                        <div className="text-xs text-muted-foreground">
                          Last synced {formatDateTime(course.last_synced_at)}
                        </div>
                      </button>
                    ))}
                  </div>
                </ScrollArea>
              )}
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0">
              <div>
                <CardTitle className="text-lg">Modules</CardTitle>
                <CardDescription>
                  Modules for {selectedCourse ? selectedCourse.name : "…"}
                </CardDescription>
              </div>
              <Button
                size="sm"
                variant="outline"
                onClick={handleRefreshModules}
                disabled={refreshingModules || !selectedCourseId}
              >
                {refreshingModules ? "Refreshing…" : "Refresh"}
              </Button>
            </CardHeader>
            <CardContent>
              {modulesError ? (
                <p className="text-sm text-destructive">{modulesError}</p>
              ) : loadingModules ? (
                <p className="text-sm text-muted-foreground">Loading modules…</p>
              ) : modules.length === 0 ? (
                <p className="text-sm text-muted-foreground">
                  {selectedCourse
                    ? "No modules found. Refresh to sync from Canvas."
                    : "Select a course to view its modules."}
                </p>
              ) : (
                <ScrollArea className="h-[420px]">
                  <div className="space-y-2">
                    {modules.map((module) => (
                      <button
                        key={module.id}
                        type="button"
                        onClick={() => setSelectedModuleId(module.id)}
                        className={cn(
                          "w-full rounded-md border px-3 py-2 text-left transition-colors hover:bg-accent",
                          selectedModuleId === module.id
                            ? "border-primary bg-accent"
                            : "border-transparent",
                        )}
                      >
                        <div className="font-medium">{module.title}</div>
                        <div className="text-xs text-muted-foreground">
                          Position {module.position ?? "—"} · Last synced {formatDateTime(module.last_synced_at)}
                        </div>
                      </button>
                    ))}
                  </div>
                </ScrollArea>
              )}
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="text-lg">Items</CardTitle>
              <CardDescription>
                Filter and select media items to view transcripts and summaries.
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex flex-col gap-3">
                <div className="grid gap-2">
                  <Input
                    placeholder="Search by item title"
                    value={filters.search}
                    onChange={(event) =>
                      setFilters((prev) => ({ ...prev, search: event.target.value }))
                    }
                  />
                  <div className="flex gap-2">
                    <select
                      className="flex h-9 w-full rounded-md border border-input bg-background px-3 py-1 text-sm shadow-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
                      value={filters.provider}
                      onChange={(event) =>
                        setFilters((prev) => ({ ...prev, provider: event.target.value }))
                      }
                    >
                      <option value="">All providers</option>
                      {providerOptions.map((provider) => (
                        <option key={provider} value={provider}>
                          {provider}
                        </option>
                      ))}
                    </select>
                    <Button
                      variant="ghost"
                      onClick={() =>
                        setFilters({
                          search: "",
                          provider: "",
                          status: [],
                        })
                      }
                    >
                      Clear
                    </Button>
                  </div>
                </div>
                <div>
                  <p className="mb-1 text-xs font-semibold uppercase text-muted-foreground">
                    Status
                  </p>
                  <div className="flex flex-wrap gap-2">
                    {statusFilters.map((status) => {
                      const active = filters.status.includes(status.value);
                      return (
                        <button
                          key={status.value}
                          type="button"
                          onClick={() =>
                            setFilters((prev) => {
                              const next = prev.status.includes(status.value)
                                ? prev.status.filter((value) => value !== status.value)
                                : [...prev.status, status.value];
                              return { ...prev, status: next };
                            })
                          }
                          className={cn(
                            "rounded-md border px-2 py-1 text-xs font-medium transition-colors hover:bg-accent",
                            active ? "border-primary bg-accent" : "border-transparent",
                          )}
                        >
                          {status.label}
                        </button>
                      );
                    })}
                  </div>
                </div>
              </div>
              <Separator />
              {itemsError ? (
                <p className="text-sm text-destructive">{itemsError}</p>
              ) : loadingItems ? (
                <p className="text-sm text-muted-foreground">Loading items…</p>
              ) : items.length === 0 ? (
                <p className="text-sm text-muted-foreground">
                  {selectedModule
                    ? "No items found for this module."
                    : "Select a module to list its items."}
                </p>
              ) : (
                <ScrollArea className="h-[320px]">
                  <div className="space-y-2">
                    {items.map((item) => {
                      const info = statusInfo[item.status];
                      return (
                        <button
                          key={item.id}
                          type="button"
                          onClick={() => setSelectedItemId(item.id)}
                          className={cn(
                            "flex w-full flex-col gap-2 rounded-md border px-3 py-2 text-left transition-colors hover:bg-accent",
                            selectedItemId === item.id
                              ? "border-primary bg-accent"
                              : "border-transparent",
                          )}
                        >
                          <div className="flex items-center justify-between gap-2">
                            <div className="font-medium">{item.title}</div>
                            <Badge variant={info.variant}>{info.label}</Badge>
                          </div>
                          <div className="flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-muted-foreground">
                            {item.provider && <span>{item.provider}</span>}
                            {item.type && <span>{item.type}</span>}
                            <span>Synced {formatDateTime(item.last_synced_at)}</span>
                          </div>
                          {item.error && (
                            <p className="text-xs text-destructive">Error: {item.error}</p>
                          )}
                        </button>
                      );
                    })}
                  </div>
                </ScrollArea>
              )}
            </CardContent>
          </Card>
        </section>

        <section>
          <Card>
            <CardHeader>
              <CardTitle className="text-lg">
                {itemDetail ? itemDetail.title : "Select an item to view details"}
              </CardTitle>
              {itemDetail && (
                <CardDescription>
                  Item #{itemDetail.id} · Module {itemDetail.module_id}
                </CardDescription>
              )}
            </CardHeader>
            <CardContent className="space-y-4">
              {detailError ? (
                <p className="text-sm text-destructive">{detailError}</p>
              ) : loadingDetail ? (
                <p className="text-sm text-muted-foreground">Loading item details…</p>
              ) : !itemDetail ? (
                <p className="text-sm text-muted-foreground">
                  Choose an item to inspect transcript jobs, media links, and artifacts.
                </p>
              ) : (
                <>
                  <div className="flex flex-wrap items-center gap-2">
                    {selectedStatusInfo && (
                      <Badge variant={selectedStatusInfo.variant}>
                        {selectedStatusInfo.label}
                      </Badge>
                    )}
                    {itemDetail.provider && (
                      <Badge variant="outline" className="capitalize">
                        {itemDetail.provider}
                      </Badge>
                    )}
                    <span className="text-xs text-muted-foreground">
                      Synced {formatDateTime(itemDetail.last_synced_at)}
                    </span>
                  </div>

                  <div className="flex flex-wrap gap-2">
                    <Button
                      onClick={handleQueueTranscript}
                      disabled={actionBusy === "transcript" || !selectedItemId}
                    >
                      {actionBusy === "transcript" ? "Queueing…" : "Fetch Transcript"}
                    </Button>
                    <Button
                      variant="secondary"
                      onClick={handleQueueSummary}
                      disabled={actionBusy === "summary" || !selectedItemId}
                    >
                      {actionBusy === "summary" ? "Queueing…" : "Summarize"}
                    </Button>
                    {itemDetail.canvas_url && (
                      <Button variant="outline" asChild>
                        <a href={itemDetail.canvas_url} target="_blank" rel="noreferrer">
                          Open in Canvas
                        </a>
                      </Button>
                    )}
                  </div>

                  <Tabs defaultValue="overview" className="w-full">
                    <TabsList>
                      <TabsTrigger value="overview">Overview</TabsTrigger>
                      <TabsTrigger value="media">Media Links</TabsTrigger>
                      <TabsTrigger value="artifacts">Artifacts</TabsTrigger>
                    </TabsList>
                    <TabsContent value="overview" className="mt-4 space-y-2 text-sm">
                      <div className="grid gap-1">
                        <span className="text-muted-foreground">Canvas ID</span>
                        <span className="font-medium">{itemDetail.id}</span>
                      </div>
                      <div className="grid gap-1">
                        <span className="text-muted-foreground">Type</span>
                        <span className="font-medium">{itemDetail.type ?? "Unknown"}</span>
                      </div>
                      <div className="grid gap-1">
                        <span className="text-muted-foreground">Transcript Path</span>
                        <span className="font-mono text-xs">
                          {itemDetail.transcript_path ?? "Not generated"}
                        </span>
                      </div>
                      <div className="grid gap-1">
                        <span className="text-muted-foreground">Summary Path</span>
                        <span className="font-mono text-xs">
                          {itemDetail.summary_path ?? "Not generated"}
                        </span>
                      </div>
                      {itemDetail.error && (
                        <div className="rounded-md border border-destructive/40 bg-destructive/10 p-3 text-destructive">
                          {itemDetail.error}
                        </div>
                      )}
                    </TabsContent>
                    <TabsContent value="media" className="mt-4">
                      {itemDetail.media_links.length === 0 ? (
                        <p className="text-sm text-muted-foreground">
                          No embedded media links detected.
                        </p>
                      ) : (
                        <ul className="space-y-2 text-sm">
                          {itemDetail.media_links.map((link, index) => (
                            <li key={`${link.provider}-${link.url}-${index}`}>
                              <span className="font-medium">{link.provider}</span>:{" "}
                              <a
                                href={link.url}
                                target="_blank"
                                rel="noreferrer"
                                className="text-primary underline"
                              >
                                {link.url}
                              </a>
                            </li>
                          ))}
                        </ul>
                      )}
                    </TabsContent>
                    <TabsContent value="artifacts" className="mt-4">
                      {itemDetail.artifacts.length === 0 ? (
                        <p className="text-sm text-muted-foreground">
                          No transcript or summary artifacts saved yet.
                        </p>
                      ) : (
                        <div className="space-y-3">
                          {itemDetail.artifacts.map((artifact) => (
                            <div
                              key={artifact.id}
                              className="flex flex-wrap items-center justify-between gap-2 rounded-md border px-3 py-2 text-sm"
                            >
                              <div className="flex flex-col">
                                <span className="font-medium capitalize">{artifact.kind}</span>
                                <span className="font-mono text-xs text-muted-foreground">
                                  {artifact.path}
                                </span>
                                <span className="text-xs text-muted-foreground">
                                  Created {formatDateTime(artifact.created_at)}
                                </span>
                              </div>
                              <Button
                                variant="outline"
                                size="sm"
                                asChild
                              >
                                <a
                                  href={`${API_BASE_URL}/items/${artifact.item_id}/${artifact.kind}/file`}
                                >
                                  Download
                                </a>
                              </Button>
                            </div>
                          ))}
                        </div>
                      )}
                    </TabsContent>
                  </Tabs>
                </>
              )}
            </CardContent>
          </Card>
        </section>
      </main>
    </div>
  );
}

export default App;
