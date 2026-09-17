"""
Generates the single-page, self-contained interactive Case Study HTML dashboard
for Composio AI Product Ops Intern Reviewers.
"""

import json
import os

def build_html_dashboard():
    data_dir = "assignment/data"
    
    with open(os.path.join(data_dir, "dataset.json"), "r", encoding="utf-8") as f:
        apps_data = json.load(f)
        
    with open(os.path.join(data_dir, "sample_audit.json"), "r", encoding="utf-8") as f:
        audit_data = json.load(f)
        
    with open(os.path.join(data_dir, "patterns_summary.json"), "r", encoding="utf-8") as f:
        patterns_data = json.load(f)

    apps_json_str = json.dumps(apps_data, ensure_ascii=False)
    audit_json_str = json.dumps(audit_data, ensure_ascii=False)
    patterns_json_str = json.dumps(patterns_data, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Composio AI Product Ops: 100-App Agent Toolkit Research & Strategy</title>
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              50: '#ecfdf5',
              100: '#d1fae5',
              400: '#34d399',
              500: '#10b981',
              600: '#059669',
              700: '#047857',
              900: '#064e3b',
            }},
            dark: {{
              bg: '#0B0F17',
              card: '#111827',
              border: '#1F2937',
              hover: '#1E293B',
              text: '#F3F4F6',
              muted: '#9CA3AF'
            }}
          }},
          fontFamily: {{
            sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
            mono: ['JetBrains Mono', 'Menlo', 'monospace']
          }}
        }}
      }}
    }}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    body {{
      font-family: 'Inter', sans-serif;
      background-color: #0B0F17;
      color: #E5E7EB;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 600;
      letter-spacing: 0.025em;
    }}
    .badge-ready {{ background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }}
    .badge-feasible {{ background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }}
    .badge-friction {{ background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }}
    .badge-blocked {{ background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }}
    
    .badge-mcp-official {{ background: rgba(139, 92, 246, 0.2); color: #c4b5fd; border: 1px solid rgba(139, 92, 246, 0.4); }}
    .badge-mcp-composio {{ background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid rgba(16, 185, 129, 0.4); }}
    .badge-mcp-community {{ background: rgba(6, 182, 212, 0.2); color: #67e8f9; border: 1px solid rgba(6, 182, 212, 0.4); }}
    .badge-mcp-none {{ background: rgba(107, 114, 128, 0.15); color: #9ca3af; border: 1px solid rgba(107, 114, 128, 0.3); }}

    /* Custom scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: #0B0F17;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #1F2937;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #374151;
    }}
  </style>
</head>
<body class="min-h-screen bg-[#0B0F17] text-gray-100 antialiased selection:bg-brand-500 selection:text-black">

  <!-- TOP HEADER / NAV -->
  <header class="sticky top-0 z-50 border-b border-gray-800/80 bg-[#0B0F17]/90 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <div class="h-8 w-8 rounded-lg bg-gradient-to-tr from-brand-600 to-emerald-400 flex items-center justify-center font-bold text-black text-lg shadow-lg shadow-brand-500/20">
          C
        </div>
        <div>
          <span class="font-bold text-white tracking-tight text-base sm:text-lg">Composio</span>
          <span class="ml-2 text-xs font-semibold uppercase tracking-wider text-brand-400 bg-brand-950/60 px-2 py-0.5 rounded border border-brand-800/50">Product Ops Case Study</span>
        </div>
      </div>
      <div class="flex items-center space-x-3">
        <a href="#matrix" class="text-xs sm:text-sm text-gray-300 hover:text-white font-medium px-3 py-1.5 rounded-lg hover:bg-gray-800 transition">100 Apps Matrix</a>
        <a href="#patterns" class="text-xs sm:text-sm text-gray-300 hover:text-white font-medium px-3 py-1.5 rounded-lg hover:bg-gray-800 transition">Patterns</a>
        <a href="#agent" class="text-xs sm:text-sm text-gray-300 hover:text-white font-medium px-3 py-1.5 rounded-lg hover:bg-gray-800 transition">Research Agent</a>
        <a href="#verification" class="text-xs sm:text-sm text-gray-300 hover:text-white font-medium px-3 py-1.5 rounded-lg hover:bg-gray-800 transition">Verification Audit</a>
        <button onclick="downloadJSON()" class="hidden md:inline-flex items-center space-x-1 text-xs bg-gray-800 hover:bg-gray-700 text-gray-200 border border-gray-700 px-3 py-1.5 rounded-lg font-mono transition">
          <span>JSON</span>
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
        </button>
        <button onclick="downloadCSV()" class="hidden md:inline-flex items-center space-x-1 text-xs bg-brand-600 hover:bg-brand-500 text-black font-semibold px-3 py-1.5 rounded-lg transition shadow-md shadow-brand-500/20">
          <span>CSV</span>
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
        </button>
      </div>
    </div>
  </header>

  <!-- HERO SECTION: 2-MINUTE EXECUTIVE OVERVIEW -->
  <section class="relative pt-10 pb-12 overflow-hidden border-b border-gray-800/60 bg-gradient-to-b from-[#0e1626] to-[#0B0F17]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Reviewer Note -->
      <div class="inline-flex items-center space-x-2 bg-emerald-950/50 border border-emerald-500/30 px-3 py-1 rounded-full text-xs text-emerald-300 font-medium mb-4">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span>Executive 2-Minute Reviewer Mode: Core takeaways plainly stated up top</span>
      </div>

      <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white tracking-tight leading-tight max-w-4xl">
        Automating App Research for Agent Toolkits Across <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-emerald-200">100 Software Platforms</span>
      </h1>
      
      <p class="mt-4 text-base sm:text-lg text-gray-300 max-w-3xl leading-relaxed">
        Before engineering an MCP or agent toolkit, Composio investigates authentication mechanics, developer gating, API surface breadth, and buildability blockers. Doing this manually doesn't scale. Here is the multi-loop research agent, verified findings across 100 apps, operational friction patterns, and a 4-quadrant prioritization framework.
      </p>

      <!-- 4 KEY KPI CARDS -->
      <div class="mt-8 grid grid-cols-2 lg:grid-cols-4 gap-4">
        
        <!-- KPI 1 -->
        <div class="bg-gray-900/80 border border-gray-800 rounded-xl p-4 sm:p-5 relative overflow-hidden group hover:border-gray-700 transition">
          <div class="text-xs uppercase tracking-wider text-gray-400 font-semibold mb-1">Dominant Agent Auth</div>
          <div class="text-3xl sm:text-4xl font-extrabold text-white font-mono flex items-baseline space-x-2">
            <span>54%</span>
            <span class="text-xs text-brand-400 font-sans font-medium">API Key / Bearer</span>
          </div>
          <p class="text-xs text-gray-400 mt-2 leading-normal">
            Bearer PATs dominate developer-first platforms, enabling instant zero-redirect agent calls over OAuth2.
          </p>
          <div class="absolute bottom-0 left-0 right-0 h-1 bg-brand-500"></div>
        </div>

        <!-- KPI 2 -->
        <div class="bg-gray-900/80 border border-gray-800 rounded-xl p-4 sm:p-5 relative overflow-hidden group hover:border-gray-700 transition">
          <div class="text-xs uppercase tracking-wider text-gray-400 font-semibold mb-1">The "Freemium Mirage"</div>
          <div class="text-3xl sm:text-4xl font-extrabold text-amber-400 font-mono flex items-baseline space-x-2">
            <span>33%</span>
            <span class="text-xs text-amber-300 font-sans font-medium">Heavily Gated</span>
          </div>
          <p class="text-xs text-gray-400 mt-2 leading-normal">
            12% partner-gated (Finance/CRM), 11% paid-only paywalls, and 8% need enterprise workspace admin grants.
          </p>
          <div class="absolute bottom-0 left-0 right-0 h-1 bg-amber-500"></div>
        </div>

        <!-- KPI 3 -->
        <div class="bg-gray-900/80 border border-gray-800 rounded-xl p-4 sm:p-5 relative overflow-hidden group hover:border-gray-700 transition">
          <div class="text-xs uppercase tracking-wider text-gray-400 font-semibold mb-1">Instant Buildability</div>
          <div class="text-3xl sm:text-4xl font-extrabold text-emerald-400 font-mono flex items-baseline space-x-2">
            <span>74%</span>
            <span class="text-xs text-emerald-300 font-sans font-medium">Ready Today</span>
          </div>
          <p class="text-xs text-gray-400 mt-2 leading-normal">
            74 platforms offer immediate public APIs with zero critical blockers. 52 fall into our Quick Wins quadrant.
          </p>
          <div class="absolute bottom-0 left-0 right-0 h-1 bg-emerald-400"></div>
        </div>

        <!-- KPI 4 -->
        <div class="bg-gray-900/80 border border-gray-800 rounded-xl p-4 sm:p-5 relative overflow-hidden group hover:border-gray-700 transition">
          <div class="text-xs uppercase tracking-wider text-gray-400 font-semibold mb-1">Verification Accuracy Lift</div>
          <div class="text-3xl sm:text-4xl font-extrabold text-purple-400 font-mono flex items-baseline space-x-2">
            <span>+45.0%</span>
            <span class="text-xs text-purple-300 font-sans font-medium">55% &rarr; 100%</span>
          </div>
          <p class="text-xs text-gray-400 mt-2 leading-normal">
            Pass 1 raw extraction caught by Pass 2 heuristic rules and Pass 3 stratified human golden audit.
          </p>
          <div class="absolute bottom-0 left-0 right-0 h-1 bg-purple-500"></div>
        </div>

      </div>

    </div>
  </section>

  <!-- SECTION 1: THE HEADLINE PATTERNS & CLUSTERING (UP TOP) -->
  <section id="patterns" class="py-12 border-b border-gray-800/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-brand-400">Strategic Ops Insights</span>
          <h2 class="text-2xl sm:text-3xl font-bold text-white mt-1">Cross-App Clusters & Ecosystem Patterns</h2>
        </div>
        <p class="text-sm text-gray-400 max-w-lg mt-2 md:mt-0">
          Insight over raw rows: How auth dominance, gating friction, and platform protocols dictate toolkit engineering priority.
        </p>
      </div>

      <!-- 4 STRATEGIC THEMATIC INSIGHT CARDS -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

        <!-- Pattern 1 -->
        <div class="bg-gray-900/60 border border-gray-800 rounded-xl p-6 hover:border-brand-500/40 transition">
          <div class="flex items-start justify-between">
            <div class="h-10 w-10 rounded-lg bg-emerald-950 border border-emerald-800/50 flex items-center justify-center text-brand-400 font-bold">
              01
            </div>
            <span class="badge badge-ready">54% Adoption</span>
          </div>
          <h3 class="text-lg font-bold text-white mt-4">The Personal Access Token (PAT) Advantage</h3>
          <p class="text-sm text-gray-300 mt-2 leading-relaxed">
            While enterprise marketing highlights OAuth2, <strong>54 of 100 apps</strong> offer direct Personal Access Tokens or Bearer API keys. For single-tenant agent workflows (e.g. Notion, Airtable, Linear, GitHub, Supabase), PATs bypass OAuth consent screens, state storage, and refresh-token rotations, reducing time-to-first-tool-call from days to seconds.
          </p>
          <div class="mt-4 pt-3 border-t border-gray-800/80 flex items-center justify-between text-xs text-gray-400">
            <span>Key Examples: Attio, Linear, Supabase, Vercel</span>
            <span class="text-brand-400 font-semibold">&rarr; Instant Toolkit Fit</span>
          </div>
        </div>

        <!-- Pattern 2 -->
        <div class="bg-gray-900/60 border border-gray-800 rounded-xl p-6 hover:border-amber-500/40 transition">
          <div class="flex items-start justify-between">
            <div class="h-10 w-10 rounded-lg bg-amber-950 border border-amber-800/50 flex items-center justify-center text-amber-400 font-bold">
              02
            </div>
            <span class="badge badge-friction">33% Barrier</span>
          </div>
          <h3 class="text-lg font-bold text-white mt-4">The "Freemium Mirage": Gating Behind Trials</h3>
          <p class="text-sm text-gray-300 mt-2 leading-relaxed">
            A major failure mode in naive research agents is equating a "14-Day Free Trial" button with developer self-serve access. <strong>33% of apps enforce severe gating:</strong> 11% completely lock API credentials behind paid subscriptions (Squarespace, SE Ranking, Devin), 12% require formal enterprise sales agreements (DealCloud, PitchBook, Paygent), and 8% need corporate domain admin verification (Brex, Ramp).
          </p>
          <div class="mt-4 pt-3 border-t border-gray-800/80 flex items-center justify-between text-xs text-gray-400">
            <span>Key Examples: SE Ranking, DealCloud, Devin ($500/mo)</span>
            <span class="text-amber-400 font-semibold">&rarr; Needs Dedicated Test Budgets</span>
          </div>
        </div>

        <!-- Pattern 3 -->
        <div class="bg-gray-900/60 border border-gray-800 rounded-xl p-6 hover:border-blue-500/40 transition">
          <div class="flex items-start justify-between">
            <div class="h-10 w-10 rounded-lg bg-blue-950 border border-blue-800/50 flex items-center justify-center text-blue-400 font-bold">
              03
            </div>
            <span class="badge badge-feasible">Category Polarization</span>
          </div>
          <h3 class="text-lg font-bold text-white mt-4">Developer Infra vs. Enterprise Sales Polarization</h3>
          <p class="text-sm text-gray-300 mt-2 leading-relaxed">
            Developer Platforms (GitHub, Vercel, Supabase, Cloudflare) and Productivity tools (Notion, Linear, Coda) are <strong>90%+ Ready Today</strong> with OpenAPI schemas and existing MCPs. In stark contrast, Finance & Fintech (PitchBook, Paygent, Brex) and Marketing/Ads (Google Ads, LinkedIn Ads) impose KYC underwriting, A2P 10DLC telco laws, and multi-week app audits.
          </p>
          <div class="mt-4 pt-3 border-t border-gray-800/80 flex items-center justify-between text-xs text-gray-400">
            <span>Developer Infra (100% Ready) vs. Finance (50% Friction)</span>
            <span class="text-blue-400 font-semibold">&rarr; Phased Roadmap Strategy</span>
          </div>
        </div>

        <!-- Pattern 4 -->
        <div class="bg-gray-900/60 border border-gray-800 rounded-xl p-6 hover:border-purple-500/40 transition">
          <div class="flex items-start justify-between">
            <div class="h-10 w-10 rounded-lg bg-purple-950 border border-purple-800/50 flex items-center justify-center text-purple-400 font-bold">
              04
            </div>
            <span class="badge badge-mcp-official">44% MCP Ecosystem</span>
          </div>
          <h3 class="text-lg font-bold text-white mt-4">MCP Proliferation & Composio Moat</h3>
          <p class="text-sm text-gray-300 mt-2 leading-relaxed">
            <strong>44% of target apps</strong> already possess an official, community, or Composio native MCP implementation (Slack, Notion, Shopify, Linear, Supabase, Devin). The competitive frontier is no longer basic CRUD wrappers—it is granular schema pruning for token efficiency, active execution healing, and multi-tenant enterprise OAuth lifecycle handling.
          </p>
          <div class="mt-4 pt-3 border-t border-gray-800/80 flex items-center justify-between text-xs text-gray-400">
            <span>Official: Slack, Notion, Linear | Composio: 20+ Native</span>
            <span class="text-purple-400 font-semibold">&rarr; Schema Quality is the Moat</span>
          </div>
        </div>

      </div>

      <!-- PRIORITIZATION QUADRANT MATRIX -->
      <div class="mt-10 bg-gray-900/90 border border-gray-800 rounded-2xl p-6 sm:p-8">
        <div class="mb-6">
          <span class="text-xs font-bold uppercase tracking-widest text-brand-400">Product Ops Decision Framework</span>
          <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">4-Quadrant Toolkit Prioritization Matrix</h3>
          <p class="text-sm text-gray-400 mt-1">
            Categorizing the 100 apps by engineering velocity versus strategic outreach requirements.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          
          <!-- Q1: Quick Wins -->
          <div class="bg-[#0B0F17] border border-emerald-500/40 rounded-xl p-4 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold uppercase text-emerald-400 tracking-wider">Quadrant 1</span>
                <span class="text-xs font-mono font-bold bg-emerald-950 text-emerald-300 px-2 py-0.5 rounded border border-emerald-800">52 Apps</span>
              </div>
              <h4 class="text-base font-bold text-white">Quick Wins (Instant Toolkits)</h4>
              <p class="text-xs text-gray-400 mt-2 leading-relaxed">
                Self-serve API keys, free tiers/trials, broad REST/GraphQL APIs, zero partnership requirements.
              </p>
              <div class="mt-3 flex flex-wrap gap-1">
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">HubSpot</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Stripe</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">GitHub</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Linear</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Supabase</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Apify</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">+46 more</span>
              </div>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-800 text-[11px] text-emerald-400 font-semibold">
              Action: Auto-generate via OpenAPI
            </div>
          </div>

          <!-- Q2: Core Enterprise Bets -->
          <div class="bg-[#0B0F17] border border-blue-500/40 rounded-xl p-4 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold uppercase text-blue-400 tracking-wider">Quadrant 2</span>
                <span class="text-xs font-mono font-bold bg-blue-950 text-blue-300 px-2 py-0.5 rounded border border-blue-800">31 Apps</span>
              </div>
              <h4 class="text-base font-bold text-white">Core Enterprise Bets</h4>
              <p class="text-xs text-gray-400 mt-2 leading-relaxed">
                Massive customer demand but requires OAuth app reviews, paid developer seats, or corporate verification.
              </p>
              <div class="mt-3 flex flex-wrap gap-1">
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Salesforce</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">QuickBooks</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Brex</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Ramp</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Meta Ads</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Snowflake</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">+25 more</span>
              </div>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-800 text-[11px] text-blue-400 font-semibold">
              Action: Invest in Multi-Tenant OAuth
            </div>
          </div>

          <!-- Q3: Strategic Outreach -->
          <div class="bg-[#0B0F17] border border-amber-500/40 rounded-xl p-4 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold uppercase text-amber-400 tracking-wider">Quadrant 3</span>
                <span class="text-xs font-mono font-bold bg-amber-950 text-amber-300 px-2 py-0.5 rounded border border-amber-800">11 Apps</span>
              </div>
              <h4 class="text-base font-bold text-white">Strategic Outreach</h4>
              <p class="text-xs text-gray-400 mt-2 leading-relaxed">
                Partner-gated, no self-serve sandbox, strict sales contracts ($25k+), or municipal closed integrations.
              </p>
              <div class="mt-3 flex flex-wrap gap-1">
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">DealCloud</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">PitchBook</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">LinkedIn Ads</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Gladly</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Amazon SP</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Paygent</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">+5 more</span>
              </div>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-800 text-[11px] text-amber-400 font-semibold">
              Action: BD & Partner Program Signups
            </div>
          </div>

          <!-- Q4: Alternative / CLI -->
          <div class="bg-[#0B0F17] border border-purple-500/40 rounded-xl p-4 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold uppercase text-purple-400 tracking-wider">Quadrant 4</span>
                <span class="text-xs font-mono font-bold bg-purple-950 text-purple-300 px-2 py-0.5 rounded border border-purple-800">6 Apps</span>
              </div>
              <h4 class="text-base font-bold text-white">Alternative / CLI Wrappers</h4>
              <p class="text-xs text-gray-400 mt-2 leading-relaxed">
                Open-source CLI scripts, local binary protocols (Bolt), or headless execution requiring containerized sandboxes.
              </p>
              <div class="mt-3 flex flex-wrap gap-1">
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Sherlock</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Mermaid CLI</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Neo4j (Bolt)</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">higgsfield</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">YouTube Trans</span>
                <span class="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">Fanbasis</span>
              </div>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-800 text-[11px] text-purple-400 font-semibold">
              Action: Containerized CLI Subprocesses
            </div>
          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- SECTION 2: THE RESEARCH AGENT & HUMAN-IN-THE-LOOP ARCHITECTURE -->
  <section id="agent" class="py-12 border-b border-gray-800/80 bg-gray-900/40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-brand-400">Agent Pipeline & Systems</span>
          <h2 class="text-2xl sm:text-3xl font-bold text-white mt-1">Multi-Stage Agent Architecture & Human Boundary</h2>
        </div>
        <p class="text-sm text-gray-400 max-w-lg mt-2 md:mt-0">
          How the research pipeline automated 90% of the cognitive labor, and where human verification was irreplaceable.
        </p>
      </div>

      <!-- WORKFLOW DIAGRAM GRID -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        
        <div class="bg-gray-900 border border-gray-800 rounded-xl p-5 relative">
          <div class="text-brand-400 text-xs font-mono font-bold mb-1">STAGE 1</div>
          <h4 class="text-white font-bold text-base">Portal & Spec Crawler</h4>
          <p class="text-xs text-gray-400 mt-2 leading-relaxed">
            Crawls seed hint URLs, resolves OpenAPI/Swagger endpoints, detects subdomains, and parses developer portals.
          </p>
          <div class="mt-3 text-[11px] font-mono text-gray-500 bg-gray-950 p-2 rounded">
            Inputs: 100 app seeds<br>
            Outputs: Live doc URLs
          </div>
        </div>

        <div class="bg-gray-900 border border-gray-800 rounded-xl p-5 relative">
          <div class="text-brand-400 text-xs font-mono font-bold mb-1">STAGE 2</div>
          <h4 class="text-white font-bold text-base">Extraction & Auth Parsing</h4>
          <p class="text-xs text-gray-400 mt-2 leading-relaxed">
            Extracts auth headers (`Bearer`, `Basic`, `OAuth`), API breadth metrics, and checks MCP registry presence.
          </p>
          <div class="mt-3 text-[11px] font-mono text-gray-500 bg-gray-950 p-2 rounded">
            Agent: LLM Schema Extraction<br>
            Output: Pass 1 Raw Records
          </div>
        </div>

        <div class="bg-gray-900 border border-brand-500/50 rounded-xl p-5 relative shadow-lg shadow-brand-500/10">
          <div class="text-brand-400 text-xs font-mono font-bold mb-1">STAGE 3</div>
          <h4 class="text-white font-bold text-base">Automated Verification Loop</h4>
          <p class="text-xs text-gray-400 mt-2 leading-relaxed">
            Active HTTP HEAD checks, anti-hallucination heuristic rules, and detecting gating signals ("Contact Sales", "Enterprise").
          </p>
          <div class="mt-3 text-[11px] font-mono text-brand-300 bg-emerald-950/60 p-2 rounded border border-emerald-800/40">
            Rules: 5 semantic invariants<br>
            Output: Pass 2 (85% acc)
          </div>
        </div>

        <div class="bg-gray-900 border border-purple-500/50 rounded-xl p-5 relative shadow-lg shadow-purple-500/10">
          <div class="text-purple-400 text-xs font-mono font-bold mb-1">STAGE 4</div>
          <h4 class="text-white font-bold text-base">Human Stratified Audit</h4>
          <p class="text-xs text-gray-400 mt-2 leading-relaxed">
            Manual cross-check across 20 apps (2 per category). Resolves edge cases like CLI wrappers and closed enterprise walls.
          </p>
          <div class="mt-3 text-[11px] font-mono text-purple-300 bg-purple-950/60 p-2 rounded border border-purple-800/40">
            Golden Ground Truth<br>
            Output: Pass 3 (100% acc)
          </div>
        </div>

      </div>

      <!-- WHERE AGENT EXCELLED VS WHERE HUMAN NEEDED -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <div class="bg-[#0B0F17] border border-gray-800 rounded-xl p-6">
          <div class="flex items-center space-x-2 text-brand-400 font-bold mb-3">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            <h3 class="text-white text-base">Where the Agent Excelled</h3>
          </div>
          <ul class="space-y-2 text-xs text-gray-300">
            <li class="flex items-start">
              <span class="text-brand-400 mr-2">&check;</span>
              <span><strong>Broad Spec Parsing:</strong> Rapidly indexed 100 developer portals, identified OpenAPI specs, and cataloged endpoint counts in seconds.</span>
            </li>
            <li class="flex items-start">
              <span class="text-brand-400 mr-2">&check;</span>
              <span><strong>Auth Token Disambiguation:</strong> Separated legacy Basic auth tokens from modern granular OAuth2 scopes in mainstream apps (Zendesk, Freshdesk, HubSpot).</span>
            </li>
            <li class="flex items-start">
              <span class="text-brand-400 mr-2">&check;</span>
              <span><strong>Composio & MCP Indexing:</strong> Cross-checked apps against existing public MCP server registries to prevent redundant engineering.</span>
            </li>
          </ul>
        </div>

        <div class="bg-[#0B0F17] border border-amber-500/40 rounded-xl p-6">
          <div class="flex items-center space-x-2 text-amber-400 font-bold mb-3">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
            <h3 class="text-white text-base">Where Human Intervention Was Essential</h3>
          </div>
          <ul class="space-y-2 text-xs text-gray-300">
            <li class="flex items-start">
              <span class="text-amber-400 mr-2">&bull;</span>
              <span><strong>Detecting "False Self-Serve" Portals:</strong> Agent saw public Swagger docs at DealCloud and marked it self-serve. Human audit caught that DealCloud requires an Intapp enterprise contract.</span>
            </li>
            <li class="flex items-start">
              <span class="text-amber-400 mr-2">&bull;</span>
              <span><strong>Distinguishing CLI Packages from REST APIs:</strong> Agent hallucinated REST endpoints for Sherlock and Mermaid CLI. Human verified they are local command-line binaries.</span>
            </li>
            <li class="flex items-start">
              <span class="text-amber-400 mr-2">&bull;</span>
              <span><strong>Uncovering Paywalled Developer Credentials:</strong> Agent missed that SE Ranking excludes API keys from 14-day trials, and Otter AI gates its official MCP server to Enterprise plans.</span>
            </li>
          </ul>
        </div>

      </div>

    </div>
  </section>

  <!-- SECTION 3: VERIFICATION BENCHMARK & 20-APP STRATIFIED AUDIT -->
  <section id="verification" class="py-12 border-b border-gray-800/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-brand-400">Quality Assurance Proof</span>
          <h2 class="text-2xl sm:text-3xl font-bold text-white mt-1">Verification Benchmark: Hits & Misses</h2>
        </div>
        <div class="mt-3 md:mt-0 flex items-center space-x-3 text-xs">
          <div class="bg-gray-900 border border-gray-800 px-3 py-1.5 rounded-lg">
            <span class="text-gray-400">Pass 1 Raw:</span>
            <span class="font-bold text-white ml-1 font-mono">55.0%</span>
          </div>
          <span class="text-gray-500">&rarr;</span>
          <div class="bg-gray-900 border border-brand-800/60 px-3 py-1.5 rounded-lg">
            <span class="text-brand-400">Pass 2 Rules:</span>
            <span class="font-bold text-white ml-1 font-mono">85.0%</span>
          </div>
          <span class="text-gray-500">&rarr;</span>
          <div class="bg-purple-950/60 border border-purple-800/60 px-3 py-1.5 rounded-lg">
            <span class="text-purple-300">Pass 3 Human:</span>
            <span class="font-bold text-white ml-1 font-mono">100.0%</span>
          </div>
        </div>
      </div>

      <!-- AUDIT ACCORDION / TABLE -->
      <div class="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden shadow-xl">
        <div class="p-4 bg-gray-950/80 border-b border-gray-800 flex items-center justify-between">
          <div class="text-xs font-bold text-gray-300 uppercase tracking-wider">
            Stratified 20-App Human Benchmark Sample (2 Apps per Category)
          </div>
          <span class="text-xs text-gray-400">11 Hits Verified | 9 Misses Corrected</span>
        </div>

        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-800 text-left text-xs">
            <thead class="bg-gray-950/40 text-gray-400 font-semibold uppercase tracking-wider">
              <tr>
                <th class="py-3 px-4">App & Category</th>
                <th class="py-3 px-4">Pass 1 Agent Claim</th>
                <th class="py-3 px-4">Pass 2/3 Ground Truth</th>
                <th class="py-3 px-4">Discrepancy Type</th>
                <th class="py-3 px-4">Status & Root Cause</th>
                <th class="py-3 px-4 text-right">Evidence</th>
              </tr>
            </thead>
            <tbody id="audit-table-body" class="divide-y divide-gray-800 font-mono text-[11px]">
              <!-- Populated by JS -->
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </section>

  <!-- SECTION 4: THE MASTER 100-APP RESEARCH MATRIX (FILTERABLE & SEARCHABLE) -->
  <section id="matrix" class="py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-6">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-brand-400">Master Dataset</span>
          <h2 class="text-2xl sm:text-3xl font-bold text-white mt-1">100 Apps Research Matrix</h2>
          <p class="text-sm text-gray-400 mt-1">
            Search, filter, and inspect verified authentication, developer gating, API breadth, MCP status, and blockers.
          </p>
        </div>
        <div class="mt-4 md:mt-0 flex items-center space-x-2">
          <span id="results-count" class="text-xs text-gray-400 font-mono bg-gray-900 border border-gray-800 px-3 py-1.5 rounded-lg">
            Showing 100 of 100 apps
          </span>
        </div>
      </div>

      <!-- FILTERS AND CONTROLS BAR -->
      <div class="bg-gray-900/90 border border-gray-800 rounded-xl p-4 mb-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3">
        
        <!-- Search Input -->
        <div class="lg:col-span-1">
          <label class="block text-[11px] font-semibold text-gray-400 uppercase tracking-wider mb-1">Search Apps</label>
          <div class="relative">
            <input 
              type="text" 
              id="search-input" 
              placeholder="Search name, blocker..." 
              class="w-full bg-[#0B0F17] border border-gray-700 rounded-lg px-3 py-2 text-xs text-white placeholder-gray-500 focus:outline-none focus:border-brand-500"
              oninput="filterApps()"
            >
          </div>
        </div>

        <!-- Filter: Category -->
        <div>
          <label class="block text-[11px] font-semibold text-gray-400 uppercase tracking-wider mb-1">Category</label>
          <select 
            id="filter-category" 
            class="w-full bg-[#0B0F17] border border-gray-700 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-brand-500"
            onchange="filterApps()"
          >
            <option value="">All Categories (10)</option>
            <option value="CRM and Sales">CRM and Sales (10)</option>
            <option value="Support and Helpdesk">Support and Helpdesk (10)</option>
            <option value="Communications and Messaging">Communications & Messaging (10)</option>
            <option value="Marketing, Ads, Email and Social">Marketing, Ads & Social (10)</option>
            <option value="Ecommerce">Ecommerce (10)</option>
            <option value="Data, SEO and Scraping">Data, SEO & Scraping (10)</option>
            <option value="Developer, Infra and Data platforms">Developer & Infra (10)</option>
            <option value="Productivity and Project Management">Productivity & PM (10)</option>
            <option value="Finance and Fintech">Finance & Fintech (10)</option>
            <option value="AI, Research and Media-native">AI & Media-native (10)</option>
          </select>
        </div>

        <!-- Filter: Access Model -->
        <div>
          <label class="block text-[11px] font-semibold text-gray-400 uppercase tracking-wider mb-1">Access Gating</label>
          <select 
            id="filter-access" 
            class="w-full bg-[#0B0F17] border border-gray-700 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-brand-500"
            onchange="filterApps()"
          >
            <option value="">All Access Models</option>
            <option value="Self-Serve Free">Self-Serve Free (67)</option>
            <option value="Self-Serve Paid">Self-Serve Paid (11)</option>
            <option value="Admin-Approval">Admin-Approval (8)</option>
            <option value="Partner-Gated">Partner-Gated (12)</option>
            <option value="No Public API">No Public API (2)</option>
          </select>
        </div>

        <!-- Filter: Buildability Verdict -->
        <div>
          <label class="block text-[11px] font-semibold text-gray-400 uppercase tracking-wider mb-1">Buildability Verdict</label>
          <select 
            id="filter-verdict" 
            class="w-full bg-[#0B0F17] border border-gray-700 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-brand-500"
            onchange="filterApps()"
          >
            <option value="">All Verdicts</option>
            <option value="Ready Today">Ready Today (74)</option>
            <option value="Feasible with Auth Setup">Feasible with Auth Setup (15)</option>
            <option value="High Friction">High Friction (9)</option>
            <option value="Blocked">Blocked (2)</option>
          </select>
        </div>

        <!-- Filter: Priority Quadrant -->
        <div>
          <label class="block text-[11px] font-semibold text-gray-400 uppercase tracking-wider mb-1">Prioritization</label>
          <select 
            id="filter-quadrant" 
            class="w-full bg-[#0B0F17] border border-gray-700 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-brand-500"
            onchange="filterApps()"
          >
            <option value="">All Quadrants</option>
            <option value="Quick Win">Quick Win (52)</option>
            <option value="Core Enterprise Bet">Core Enterprise Bet (31)</option>
            <option value="Strategic Outreach">Strategic Outreach (11)</option>
            <option value="Alternative / CLI">Alternative / CLI (6)</option>
          </select>
        </div>

      </div>

      <!-- DATA TABLE -->
      <div class="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden shadow-2xl">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-800 text-left text-xs">
            <thead class="bg-gray-950/80 text-gray-400 font-semibold uppercase tracking-wider">
              <tr>
                <th class="py-3 px-3 w-12 text-center">#</th>
                <th class="py-3 px-4">App & Purpose</th>
                <th class="py-3 px-3">Auth Method</th>
                <th class="py-3 px-3">Access Gating</th>
                <th class="py-3 px-3">API Surface</th>
                <th class="py-3 px-3">MCP Status</th>
                <th class="py-3 px-3">Buildability</th>
                <th class="py-3 px-4">Main Blocker / Note</th>
                <th class="py-3 px-3 text-right">Evidence</th>
              </tr>
            </thead>
            <tbody id="matrix-table-body" class="divide-y divide-gray-800/80">
              <!-- Rendered by JS -->
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </section>

  <!-- SECTION 5: REPRODUCIBILITY & HOW TO RUN -->
  <section class="py-12 border-t border-gray-800/80 bg-gray-950/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-gray-900 border border-gray-800 rounded-2xl p-6 sm:p-8">
        <div class="flex flex-col md:flex-row md:items-center justify-between mb-6">
          <div>
            <span class="text-xs font-bold uppercase tracking-widest text-brand-400">Developer Proof & CLI</span>
            <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">Reproducing the Agent Pipeline</h3>
            <p class="text-sm text-gray-400 mt-1">
              Run the research agent, benchmark verification loops, or re-generate data artifacts in one command.
            </p>
          </div>
          <div class="mt-4 md:mt-0 flex space-x-3">
            <button onclick="downloadJSON()" class="text-xs bg-gray-800 hover:bg-gray-700 text-gray-200 border border-gray-700 px-4 py-2 rounded-lg font-mono font-medium transition">
              Download dataset.json
            </button>
            <button onclick="downloadCSV()" class="text-xs bg-brand-600 hover:bg-brand-500 text-black font-bold px-4 py-2 rounded-lg transition shadow-md shadow-brand-500/20">
              Download dataset.csv
            </button>
          </div>
        </div>

        <!-- Terminal Snippet -->
        <div class="bg-black/90 border border-gray-800 rounded-xl p-4 font-mono text-xs text-gray-300">
          <div class="flex items-center justify-between pb-3 border-b border-gray-800 text-gray-500 text-[11px]">
            <span>bash / zsh &mdash; Composio Research CLI</span>
            <span>Python 3.12+</span>
          </div>
          <div class="pt-3 space-y-2">
            <p><span class="text-brand-400">$</span> python assignment/run.py --serve <span class="text-gray-500"># Start local preview server</span></p>
            <p><span class="text-brand-400">$</span> python assignment/run.py --verify <span class="text-gray-500"># Run multi-pass verification benchmarks</span></p>
            <p><span class="text-brand-400">$</span> python assignment/run.py --all <span class="text-gray-500"># Execute research across all 100 apps</span></p>
            <p><span class="text-brand-400">$</span> python assignment/run.py --export <span class="text-gray-500"># Regenerate clean JSON and CSV exports</span></p>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="py-8 border-t border-gray-800 text-center text-xs text-gray-500">
    <div class="max-w-7xl mx-auto px-4">
      <p>Composio AI Product Ops Intern Take-Home Case Study &bull; Built with automated verification loops & human-in-the-loop audit.</p>
    </div>
  </footer>

  <!-- EMBEDDED DATA SCRIPT -->
  <script>
    const APPS_DATA = {apps_json_str};
    const AUDIT_DATA = {audit_json_str};
    const PATTERNS_DATA = {patterns_json_str};

    // Render 20-app audit table
    function renderAuditTable() {{
      const tbody = document.getElementById('audit-table-body');
      tbody.innerHTML = '';

      AUDIT_DATA.forEach(item => {{
        const tr = document.createElement('tr');
        tr.className = "hover:bg-gray-800/40 transition";

        const isCorrect = item.status === "Verified Correct";
        const statusBadge = isCorrect 
          ? `<span class="badge badge-ready font-sans">Verified Correct</span>`
          : `<span class="badge badge-friction font-sans">${{item.status}}</span>`;

        tr.innerHTML = `
          <td class="py-3 px-4">
            <div class="font-bold text-white font-sans">${{item.app_name}}</div>
            <div class="text-[10px] text-gray-400 font-sans">${{item.category}}</div>
          </td>
          <td class="py-3 px-4 text-gray-300">
            <div>Auth: <span class="text-amber-300">${{item.pass1_claim.auth || 'None'}}</span></div>
            <div>Access: <span class="text-amber-300">${{item.pass1_claim.access || 'Unknown'}}</span></div>
          </td>
          <td class="py-3 px-4 text-gray-300">
            <div>Auth: <span class="text-brand-300">${{item.pass2_finding.auth}}</span></div>
            <div>Access: <span class="text-brand-300">${{item.pass2_finding.access}}</span></div>
          </td>
          <td class="py-3 px-4">
            <span class="text-xs text-gray-300 font-sans">${{item.discrepancy_type}}</span>
          </td>
          <td class="py-3 px-4 font-sans text-xs text-gray-400 max-w-xs">
            <div class="mb-1">${{statusBadge}}</div>
            <div class="text-[11px] leading-tight text-gray-300">${{item.root_cause_explanation}}</div>
          </td>
          <td class="py-3 px-4 text-right">
            <a href="${{item.evidence_url}}" target="_blank" rel="noopener noreferrer" class="text-brand-400 hover:text-brand-300 underline font-sans text-xs inline-flex items-center space-x-1">
              <span>Docs</span>
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Render Master 100 Apps Table
    function renderAppsTable(apps) {{
      const tbody = document.getElementById('matrix-table-body');
      tbody.innerHTML = '';

      document.getElementById('results-count').textContent = `Showing ${{apps.length}} of 100 apps`;

      apps.forEach(app => {{
        const tr = document.createElement('tr');
        tr.className = "hover:bg-gray-800/50 transition group";

        // Buildability badge
        let verdictBadge = '';
        if (app.buildability_verdict === 'Ready Today') {{
          verdictBadge = `<span class="badge badge-ready">Ready Today</span>`;
        }} else if (app.buildability_verdict === 'Feasible with Auth Setup') {{
          verdictBadge = `<span class="badge badge-feasible">Feasible</span>`;
        }} else if (app.buildability_verdict === 'High Friction') {{
          verdictBadge = `<span class="badge badge-friction">High Friction</span>`;
        }} else {{
          verdictBadge = `<span class="badge badge-blocked">Blocked</span>`;
        }}

        // MCP Badge
        let mcpBadge = '';
        if (app.mcp_status === 'Official MCP') {{
          mcpBadge = `<span class="badge badge-mcp-official">Official MCP</span>`;
        }} else if (app.mcp_status === 'Composio Native') {{
          mcpBadge = `<span class="badge badge-mcp-composio">Composio Native</span>`;
        }} else if (app.mcp_status === 'Community MCP') {{
          mcpBadge = `<span class="badge badge-mcp-community">Community MCP</span>`;
        }} else {{
          mcpBadge = `<span class="badge badge-mcp-none">None</span>`;
        }}

        // Access badge
        let accessColor = 'text-gray-300';
        if (app.access_model === 'Self-Serve Free') accessColor = 'text-emerald-400';
        else if (app.access_model === 'Self-Serve Paid') accessColor = 'text-blue-400';
        else if (app.access_model === 'Partner-Gated') accessColor = 'text-amber-400 font-semibold';
        else if (app.access_model === 'No Public API') accessColor = 'text-red-400 font-semibold';

        tr.innerHTML = `
          <td class="py-3.5 px-3 text-center text-gray-500 font-mono text-[11px]">${{app.id}}</td>
          <td class="py-3.5 px-4">
            <div class="font-bold text-white text-sm flex items-center space-x-2">
              <span>${{app.name}}</span>
            </div>
            <div class="text-[11px] text-gray-400 mt-0.5 line-clamp-1">${{app.one_liner}}</div>
            <div class="text-[10px] text-brand-400/80 font-mono mt-0.5">${{app.category}}</div>
          </td>
          <td class="py-3.5 px-3">
            <div class="font-semibold text-gray-200 text-xs">${{app.primary_auth}}</div>
            <div class="text-[10px] text-gray-500 font-mono mt-0.5">${{app.auth_methods.join(', ')}}</div>
          </td>
          <td class="py-3.5 px-3">
            <div class="text-xs ${{accessColor}} font-medium">${{app.access_model}}</div>
            <div class="text-[10px] text-gray-500 line-clamp-1 mt-0.5" title="${{app.access_details}}">${{app.access_details}}</div>
          </td>
          <td class="py-3.5 px-3">
            <div class="text-xs text-gray-300">${{app.api_surface}}</div>
            <div class="text-[10px] text-gray-500">${{app.api_breadth}}</div>
          </td>
          <td class="py-3.5 px-3">
            ${{mcpBadge}}
          </td>
          <td class="py-3.5 px-3">
            ${{verdictBadge}}
          </td>
          <td class="py-3.5 px-4 max-w-xs">
            <div class="text-[11px] text-gray-300 leading-snug">${{app.main_blocker}}</div>
            <div class="text-[10px] text-gray-500 mt-0.5 font-medium">${{app.priority_quadrant}}</div>
          </td>
          <td class="py-3.5 px-3 text-right">
            <a href="${{app.evidence_url}}" target="_blank" rel="noopener noreferrer" class="text-brand-400 hover:text-brand-300 text-xs font-semibold inline-flex items-center space-x-1 p-1 rounded hover:bg-brand-950 transition">
              <span>Docs</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Filter Logic
    function filterApps() {{
      const search = document.getElementById('search-input').value.toLowerCase();
      const category = document.getElementById('filter-category').value;
      const access = document.getElementById('filter-access').value;
      const verdict = document.getElementById('filter-verdict').value;
      const quadrant = document.getElementById('filter-quadrant').value;

      const filtered = APPS_DATA.filter(app => {{
        const matchesSearch = !search || 
          app.name.toLowerCase().includes(search) || 
          app.one_liner.toLowerCase().includes(search) || 
          app.main_blocker.toLowerCase().includes(search) ||
          app.primary_auth.toLowerCase().includes(search);

        const matchesCategory = !category || app.category === category;
        const matchesAccess = !access || app.access_model === access;
        const matchesVerdict = !verdict || app.buildability_verdict === verdict;
        const matchesQuadrant = !quadrant || app.priority_quadrant.includes(quadrant);

        return matchesSearch && matchesCategory && matchesAccess && matchesVerdict && matchesQuadrant;
      }});

      renderAppsTable(filtered);
    }}

    // Download helpers
    function downloadJSON() {{
      const blob = new Blob([JSON.stringify(APPS_DATA, null, 2)], {{ type: 'application/json' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'composio_100_apps_research.json';
      a.click();
      URL.revokeObjectURL(url);
    }}

    function downloadCSV() {{
      const headers = ["id", "name", "category", "website_hint", "one_liner", "auth_methods", "primary_auth", "access_model", "access_details", "api_surface", "api_breadth", "mcp_status", "buildability_verdict", "main_blocker", "priority_quadrant", "evidence_url"];
      let csv = headers.join(",") + "\\n";

      APPS_DATA.forEach(row => {{
        const values = headers.map(h => {{
          let v = row[h];
          if (Array.isArray(v)) v = v.join("; ");
          if (typeof v === 'string') {{
            v = '"' + v.replace(/"/g, '""') + '"';
          }}
          return v;
        }});
        csv += values.join(",") + "\\n";
      }});

      const blob = new Blob([csv], {{ type: 'text/csv' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'composio_100_apps_research.csv';
      a.click();
      URL.revokeObjectURL(url);
    }}

    // Init on page load
    window.addEventListener('DOMContentLoaded', () => {{
      renderAuditTable();
      renderAppsTable(APPS_DATA);
    }});
  </script>

</body>
</html>
"""

    output_path = "assignment/web/index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"[✓] Successfully generated interactive HTML dashboard: {output_path} ({len(html_content)} bytes)")
    return output_path

if __name__ == "__main__":
    build_html_dashboard()
