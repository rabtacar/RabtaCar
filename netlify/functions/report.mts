// POST /api/report  — called by the tag page when someone taps an issue button.
// Validates input, then forwards to Google Apps Script with the shared secret.
// The owner's phone number never reaches the browser.
import type { Config, Context } from "@netlify/functions"

const ISSUES = new Set(["towing", "parking", "lights", "door", "emergency", "other"])
const TAG_RE = /^RBC-[A-Z0-9]{5,10}$/

export default async (req: Request, context: Context) => {
  let body: any
  try {
    body = await req.json()
  } catch {
    return Response.json({ ok: false, error: "bad_json" }, { status: 400 })
  }

  const tag = String(body.tag || "").trim().toUpperCase()
  const issue = String(body.issue || "").toLowerCase()
  const note = String(body.note || "").replace(/\s+/g, " ").trim().slice(0, 120)

  if (!TAG_RE.test(tag)) return Response.json({ ok: false, error: "bad_tag" }, { status: 400 })
  if (!ISSUES.has(issue)) return Response.json({ ok: false, error: "bad_issue" }, { status: 400 })
  if (issue === "other" && note.length < 3)
    return Response.json({ ok: false, error: "note_required" }, { status: 400 })

  const res = await fetch(Netlify.env.get("APPS_SCRIPT_URL")!, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      secret: Netlify.env.get("RABTA_SECRET"),
      tag,
      issue,
      note,
      source: "web",
    }),
  })

  const data = await res.json().catch(() => ({ ok: false, error: "backend_error" }))
  // Pass back only status info
  return Response.json({ ok: !!data.ok, status: data.status, error: data.error }, { status: data.ok ? 200 : 502 })
}

export const config: Config = {
  path: "/api/report",
  method: "POST",
  // Stop one person from spamming: 5 reports per minute per IP
  rateLimit: { windowLimit: 5, windowSize: 60, aggregateBy: ["ip", "domain"] },
}
