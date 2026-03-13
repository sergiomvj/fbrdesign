import { NextResponse } from "next/server";

import { getAssetVersions } from "@/lib/api";

export async function GET() {
  const payload = await getAssetVersions();
  return NextResponse.json(payload);
}
