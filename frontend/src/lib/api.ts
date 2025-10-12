import { API_BASE_URL } from "@/config";
import type {
  Course,
  Item,
  ItemDetail,
  ItemStatus,
  Module,
  RefreshResult,
} from "@/types";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers ?? {}),
    },
    ...init,
  });
  if (!response.ok) {
    const text = await response.text();
    throw new Error(text || `Request failed with status ${response.status}`);
  }
  if (response.status === 204) {
    return undefined as T;
  }
  return (await response.json()) as T;
}

export function getHealth(): Promise<{ status: string }> {
  return request("/health");
}

export function listCourses(): Promise<Course[]> {
  return request("/courses");
}

export function refreshCourses(): Promise<RefreshResult> {
  return request("/me/courses/refresh", { method: "POST" });
}

export function listModules(courseId: number): Promise<Module[]> {
  return request(`/courses/${courseId}/modules`);
}

export function refreshModules(courseId: number): Promise<RefreshResult> {
  return request(`/courses/${courseId}/modules/refresh`, { method: "POST" });
}

export interface ItemFilters {
  moduleId?: number;
  courseId?: number;
  status?: ItemStatus[];
  provider?: string;
  search?: string;
}

export async function listItems(filters: ItemFilters): Promise<Item[]> {
  const params = new URLSearchParams();
  if (filters.moduleId != null) {
    params.set("module_id", String(filters.moduleId));
  } else if (filters.courseId != null) {
    params.set("course_id", String(filters.courseId));
  }
  if (filters.status?.length) {
    for (const status of filters.status) {
      params.append("status", status);
    }
  }
  if (filters.provider) {
    params.set("provider", filters.provider);
  }
  if (filters.search) {
    params.set("search", filters.search);
  }
  const query = params.toString();
  const suffix = query ? `?${query}` : "";
  return request(`/items${suffix}`);
}

export function getItemDetail(itemId: number): Promise<ItemDetail> {
  return request(`/items/${itemId}`);
}

export function queueTranscript(itemId: number): Promise<{ status: string }> {
  return request(`/items/${itemId}/fetch-transcript`, { method: "POST" });
}

export function queueSummary(itemId: number): Promise<{ status: string }> {
  return request(`/items/${itemId}/summarize`, { method: "POST" });
}
