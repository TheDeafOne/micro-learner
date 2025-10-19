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
import { statusFilters, statusInfo } from "@/constants/status";
import type { DashboardFilters } from "@/hooks/useDashboardData";
import { formatDateTime } from "@/lib/format";
import { cn } from "@/lib/utils";
import type { Item, ItemStatus } from "@/types";

interface ItemPanelProps {
  items: Item[];
  selectedItemId: number | null;
  onSelectItem: (itemId: number) => void;
  loading: boolean;
  error: string | null;
  filters: DashboardFilters;
  onSearchChange: (value: string) => void;
  onProviderChange: (value: string) => void;
  onResetFilters: () => void;
  onToggleStatus: (value: ItemStatus) => void;
  providerOptions: string[];
  selectedModuleTitle: string | null;
}

export function ItemPanel({
  items,
  selectedItemId,
  onSelectItem,
  loading,
  error,
  filters,
  onSearchChange,
  onProviderChange,
  onResetFilters,
  onToggleStatus,
  providerOptions,
  selectedModuleTitle,
}: ItemPanelProps) {
  return (
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
              onChange={(event) => onSearchChange(event.target.value)}
            />
            <div className="flex gap-2">
              <select
                className="flex h-9 w-full rounded-md border border-input bg-background px-3 py-1 text-sm shadow-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
                value={filters.provider}
                onChange={(event) => onProviderChange(event.target.value)}
              >
                <option value="">All providers</option>
                {providerOptions.map((provider) => (
                  <option key={provider} value={provider}>
                    {provider}
                  </option>
                ))}
              </select>
              <Button variant="ghost" onClick={onResetFilters}>
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
                    onClick={() => onToggleStatus(status.value)}
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
        {error ? (
          <p className="text-sm text-destructive">{error}</p>
        ) : loading ? (
          <p className="text-sm text-muted-foreground">Loading items…</p>
        ) : items.length === 0 ? (
          <p className="text-sm text-muted-foreground">
            {selectedModuleTitle
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
                    onClick={() => onSelectItem(item.id)}
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
  );
}
