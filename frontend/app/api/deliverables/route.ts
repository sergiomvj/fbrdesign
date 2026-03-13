import { NextResponse } from "next/server";

import { getDeliverables } from "@/lib/api";

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const designRequestId = searchParams.get("design_request_id") ?? undefined;
  const payload = await getDeliverables(designRequestId);
  return NextResponse.json(payload);
}
