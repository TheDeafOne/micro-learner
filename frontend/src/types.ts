export type ItemStatus = "DISCOVERED" | "TRANSCRIPT_READY" | "SUMMARY_READY" | "FAILED";

export interface Course {
  id: number;
  name: string;
  last_synced_at?: string | null;
}

export interface Module {
  id: number;
  course_id: number;
  title: string;
  position?: number | null;
  last_synced_at?: string | null;
}

export interface Item {
  id: number;
  module_id: number;
  type?: string | null;
  title: string;
  canvas_url?: string | null;
  provider?: string | null;
  status: ItemStatus;
  error?: string | null;
  last_synced_at?: string | null;
}

export interface MediaLink {
  provider: string;
  url: string;
}

export interface Artifact {
  id: number;
  item_id: number;
  kind: string;
  path: string;
  created_at: string;
}

export interface ItemDetail extends Item {
  transcript_path?: string | null;
  summary_path?: string | null;
  artifacts: Artifact[];
  media_links: MediaLink[];
}

export interface RefreshResult {
  count: number;
  detail: string;
}
