import { NextResponse } from "next/server";

import { getDesignRequests } from "@/lib/api";

export async function GET() {
  const payload = await getDesignRequests();
  return NextResponse.json(payload);
}

export async function POST(request: Request) {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  const payload = await request.json();

  if (!backendUrl) {
    const timestamp = new Date().toISOString();

    return NextResponse.json(
      {
        data: {
          ...payload,
          id: crypto.randomUUID(),
          round_number: 1,
          requested_at: timestamp,
          approved_at: null,
          delivered_at: null,
          created_at: timestamp,
          updated_at: timestamp,
        },
        meta: { count: 1 },
        error: null,
      },
      { status: 201 },
    );
  }

  const response = await fetch(`${backendUrl}/api/design-requests`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  const body = await response.json();
  return NextResponse.json(body, { status: response.status });
}
