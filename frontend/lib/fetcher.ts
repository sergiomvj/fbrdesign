export class FetcherError extends Error {
  status: number;

  constructor(message: string, status: number) {
    super(message);
    this.name = "FetcherError";
    this.status = status;
  }
}

export async function fetcher<T>(input: string, init?: RequestInit): Promise<T> {
  const response = await fetch(input, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers ?? {}),
    },
    cache: "no-store",
  });

  if (!response.ok) {
    throw new FetcherError("Nao foi possivel concluir a requisicao.", response.status);
  }

  return (await response.json()) as T;
}
