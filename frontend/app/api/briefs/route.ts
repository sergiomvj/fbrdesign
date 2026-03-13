import { NextResponse } from "next/server";

import { getBriefs } from "@/lib/api";

export async function GET() {
  const payload = await getBriefs();
  return NextResponse.json(payload);
}

export async function POST(request: Request) {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  const payload = await request.json();

  if (!backendUrl) {
    return NextResponse.json(
      {
        data: {
          ...payload,
          id: crypto.randomUUID(),
          created_at: new Date().toISOString(),
          updated_at: new Date().toISOString(),
        },
        meta: { count: 1 },
        error: null,
      },
      { status: 201 },
    );
  }

  const response = await fetch(`${backendUrl}/api/briefs`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  const body = await response.json();
  return NextResponse.json(body, { status: response.status });
}
