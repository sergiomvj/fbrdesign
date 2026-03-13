import { NextResponse } from "next/server";

import { getApprovalSteps } from "@/lib/api";

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const designRequestId = searchParams.get("design_request_id") ?? undefined;
  const payload = await getApprovalSteps(designRequestId);
  return NextResponse.json(payload);
}

export async function POST(request: Request) {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  const payload = await request.json();

  if (!backendUrl) {
    const timestamp = new Date().toISOString();

    return NextResponse.json(
      {
        ...payload,
        id: crypto.randomUUID(),
        decided_at: null,
        created_at: timestamp,
        updated_at: timestamp,
      },
      { status: 201 },
    );
  }

  const response = await fetch(`${backendUrl}/api/approval-steps`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  const body = await response.json();
  return NextResponse.json(body, { status: response.status });
}
