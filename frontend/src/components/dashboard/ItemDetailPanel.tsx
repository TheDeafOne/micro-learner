import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { statusInfo } from "@/constants/status";
import type { DashboardAction } from "@/hooks/useDashboardData";
import { formatDateTime } from "@/lib/format";
import type { ItemDetail } from "@/types";

interface ItemDetailPanelProps {
  itemDetail: ItemDetail | null;
  loading: boolean;
  error: string | null;
  actionBusy: DashboardAction;
  apiBaseUrl: string;
  onQueueTranscript: () => Promise<void>;
  onQueueSummary: () => Promise<void>;
}

export function ItemDetailPanel({
  itemDetail,
  loading,
  error,
  actionBusy,
  apiBaseUrl,
  onQueueTranscript,
  onQueueSummary,
}: ItemDetailPanelProps) {
  const selectedStatusInfo = itemDetail ? statusInfo[itemDetail.status] : null;

  return (
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
        {error ? (
          <p className="text-sm text-destructive">{error}</p>
        ) : loading ? (
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
                onClick={onQueueTranscript}
                disabled={actionBusy === "transcript" || !itemDetail}
              >
                {actionBusy === "transcript" ? "Queueing…" : "Fetch Transcript"}
              </Button>
              <Button
                variant="secondary"
                onClick={onQueueSummary}
                disabled={actionBusy === "summary" || !itemDetail}
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
                        <Button variant="outline" size="sm" asChild>
                          <a
                            href={`${apiBaseUrl}/items/${artifact.item_id}/${artifact.kind}/file`}
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
  );
}
