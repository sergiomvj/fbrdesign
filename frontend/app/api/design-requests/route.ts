import { NextResponse } from "next/server";

import { getDesignRequests } from "@/lib/api";

export async function GET() {
  const payload = await getDesignRequests();
  return NextResponse.json(payload);
}
