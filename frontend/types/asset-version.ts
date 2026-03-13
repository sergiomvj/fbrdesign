export interface AssetVersion {
  id: string;
  asset_file_id: string;
  version_number: number;
  derived_from_version_id?: string | null;
  storage_key: string;
  storage_bucket: string;
  mime_type: string;
  file_size_bytes: number;
  checksum: string;
  origin_type: string;
  change_summary?: string | null;
  is_final: boolean;
  approved_by_name?: string | null;
  approved_at?: string | null;
  created_at: string;
}

export interface AssetVersionListResponse {
  data: AssetVersion[];
  meta: { count: number };
  error: null;
}
