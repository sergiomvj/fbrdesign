function StatusBadge({ value }: { value: string }) {
  const color =
    value === "urgent" || value === "changes_requested"
      ? "#ef4444"
      : value.includes("approval")
        ? "#f59e0b"
        : value === "in_production"
          ? "#38bdf8"
          : "#22c55e";

  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        padding: "6px 10px",
        borderRadius: 999,
        border: `1px solid ${color}44`,
        color,
        fontSize: 12,
        textTransform: "uppercase",
        letterSpacing: "0.08em",
      }}
    >
      {value}
    </span>
  );
}

export { StatusBadge };
