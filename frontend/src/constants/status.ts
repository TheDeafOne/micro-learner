import type { ItemStatus } from "@/types";

export const statusInfo: Record<
  ItemStatus,
  { label: string; variant: "default" | "secondary" | "destructive" | "outline" }
> = {
  DISCOVERED: { label: "Discovered", variant: "outline" },
  TRANSCRIPT_READY: { label: "Transcript Ready", variant: "secondary" },
  SUMMARY_READY: { label: "Summary Ready", variant: "default" },
  FAILED: { label: "Failed", variant: "destructive" },
};

export const statusFilters: { value: ItemStatus; label: string }[] = [
  { value: "DISCOVERED", label: "Discovered" },
  { value: "TRANSCRIPT_READY", label: "Transcript Ready" },
  { value: "SUMMARY_READY", label: "Summary Ready" },
  { value: "FAILED", label: "Failed" },
];
