import Link from "next/link";
import type { ReactNode } from "react";

const navItems = [
  { href: "/", label: "Overview" },
  { href: "/intake", label: "Intake" },
  { href: "/requests", label: "Requests" },
  { href: "/reviews", label: "Reviews" },
];

export default function StudioLayout({ children }: { children: ReactNode }) {
  return (
    <div style={{ display: "grid", gridTemplateColumns: "240px 1fr", minHeight: "100vh" }}>
      <aside
        style={{
          borderRight: "1px solid rgba(148,163,184,0.16)",
          padding: "24px 18px",
          background: "rgba(6, 13, 24, 0.7)",
        }}
      >
        <div style={{ fontSize: 24, fontWeight: 700, marginBottom: 24 }}>FBR-Design</div>
        <nav style={{ display: "grid", gap: 12 }}>
          {navItems.map((item) => (
            <Link key={item.href} href={item.href} style={{ color: "#c8d6eb" }}>
              {item.label}
            </Link>
          ))}
        </nav>
      </aside>
      <main style={{ padding: 28 }}>{children}</main>
    </div>
  );
}
