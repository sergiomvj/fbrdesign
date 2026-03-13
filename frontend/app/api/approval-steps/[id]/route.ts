import { NextResponse } from "next/server";

export async function PATCH(
  request: Request,
  { params }: { params: Promise<{ id: string }> },
) {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  const payload = await request.json();
  const { id } = await params;

  if (!backendUrl) {
    return NextResponse.json(
      {
        id,
        ...payload,
        updated_at: new Date().toISOString(),
      },
      { status: 200 },
    );
  }

  const response = await fetch(`${backendUrl}/api/approval-steps/${id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  const body = await response.json();
  return NextResponse.json(body, { status: response.status });
}
