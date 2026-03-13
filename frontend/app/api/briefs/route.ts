import { NextResponse } from "next/server";

import { getBriefs } from "@/lib/api";

export async function GET() {
  const payload = await getBriefs();
  return NextResponse.json(payload);
}
