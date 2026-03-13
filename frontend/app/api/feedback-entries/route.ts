import { NextResponse } from "next/server";

import { getFeedbackEntries } from "@/lib/api";

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const threadId = searchParams.get("thread_id") ?? undefined;
  const payload = await getFeedbackEntries(threadId);
  return NextResponse.json(payload);
}
