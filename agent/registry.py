"""
Registry of 100 Apps for Composio AI Product Ops Take-Home Research.
Contains canonical IDs, names, categories, and seed hint URLs.
"""

APPS_REGISTRY = [
    # 1. CRM and Sales
    {"id": 1, "name": "Salesforce", "category": "CRM and Sales", "website_hint": "salesforce.com"},
    {"id": 2, "name": "HubSpot", "category": "CRM and Sales", "website_hint": "hubspot.com"},
    {"id": 3, "name": "Pipedrive", "category": "CRM and Sales", "website_hint": "pipedrive.com"},
    {"id": 4, "name": "Attio", "category": "CRM and Sales", "website_hint": "attio.com"},
    {"id": 5, "name": "Twenty", "category": "CRM and Sales", "website_hint": "twenty.com (open-source CRM)"},
    {"id": 6, "name": "Podio", "category": "CRM and Sales", "website_hint": "podio.com"},
    {"id": 7, "name": "Zoho CRM", "category": "CRM and Sales", "website_hint": "zoho.com/crm"},
    {"id": 8, "name": "Close", "category": "CRM and Sales", "website_hint": "close.com"},
    {"id": 9, "name": "Copper", "category": "CRM and Sales", "website_hint": "copper.com"},
    {"id": 10, "name": "DealCloud", "category": "CRM and Sales", "website_hint": "api.docs.dealcloud.com"},

    # 2. Support and Helpdesk
    {"id": 11, "name": "Zendesk", "category": "Support and Helpdesk", "website_hint": "zendesk.com"},
    {"id": 12, "name": "Intercom", "category": "Support and Helpdesk", "website_hint": "intercom.com"},
    {"id": 13, "name": "Freshdesk", "category": "Support and Helpdesk", "website_hint": "freshdesk.com"},
    {"id": 14, "name": "Front", "category": "Support and Helpdesk", "website_hint": "front.com"},
    {"id": 15, "name": "Pylon", "category": "Support and Helpdesk", "website_hint": "usepylon.com"},
    {"id": 16, "name": "LiveAgent", "category": "Support and Helpdesk", "website_hint": "liveagent.com"},
    {"id": 17, "name": "Plain", "category": "Support and Helpdesk", "website_hint": "plain.com"},
    {"id": 18, "name": "Help Scout", "category": "Support and Helpdesk", "website_hint": "helpscout.com"},
    {"id": 19, "name": "Gorgias", "category": "Support and Helpdesk", "website_hint": "gorgias.com"},
    {"id": 20, "name": "Gladly", "category": "Support and Helpdesk", "website_hint": "gladly.com"},

    # 3. Communications and Messaging
    {"id": 21, "name": "Slack", "category": "Communications and Messaging", "website_hint": "slack.com"},
    {"id": 22, "name": "Twilio", "category": "Communications and Messaging", "website_hint": "twilio.com"},
    {"id": 23, "name": "Zoho Cliq", "category": "Communications and Messaging", "website_hint": "zoho.com/cliq"},
    {"id": 24, "name": "Lark (Larksuite)", "category": "Communications and Messaging", "website_hint": "open.larksuite.com"},
    {"id": 25, "name": "Pumble", "category": "Communications and Messaging", "website_hint": "pumble.com"},
    {"id": 26, "name": "Discord", "category": "Communications and Messaging", "website_hint": "discord.com"},
    {"id": 27, "name": "Telegram", "category": "Communications and Messaging", "website_hint": "core.telegram.org"},
    {"id": 28, "name": "WhatsApp Business", "category": "Communications and Messaging", "website_hint": "developers.facebook.com/docs/whatsapp"},
    {"id": 29, "name": "Aircall", "category": "Communications and Messaging", "website_hint": "aircall.io"},
    {"id": 30, "name": "Vonage", "category": "Communications and Messaging", "website_hint": "developer.vonage.com"},

    # 4. Marketing, Ads, Email and Social
    {"id": 31, "name": "Google Ads", "category": "Marketing, Ads, Email and Social", "website_hint": "developers.google.com/google-ads"},
    {"id": 32, "name": "Meta Ads", "category": "Marketing, Ads, Email and Social", "website_hint": "developers.facebook.com/docs/marketing-apis"},
    {"id": 33, "name": "LinkedIn Ads", "category": "Marketing, Ads, Email and Social", "website_hint": "learn.microsoft.com/linkedin/marketing"},
    {"id": 34, "name": "GoHighLevel", "category": "Marketing, Ads, Email and Social", "website_hint": "highlevel.stoplight.io"},
    {"id": 35, "name": "Mailchimp", "category": "Marketing, Ads, Email and Social", "website_hint": "mailchimp.com/developer"},
    {"id": 36, "name": "Klaviyo", "category": "Marketing, Ads, Email and Social", "website_hint": "developers.klaviyo.com"},
    {"id": 37, "name": "systeme.io", "category": "Marketing, Ads, Email and Social", "website_hint": "systeme.io (funnel builder)"},
    {"id": 38, "name": "Pinterest", "category": "Marketing, Ads, Email and Social", "website_hint": "developers.pinterest.com"},
    {"id": 39, "name": "Threads (Meta)", "category": "Marketing, Ads, Email and Social", "website_hint": "developers.facebook.com/docs/threads"},
    {"id": 40, "name": "SendGrid", "category": "Marketing, Ads, Email and Social", "website_hint": "sendgrid.com"},

    # 5. Ecommerce
    {"id": 41, "name": "Shopify", "category": "Ecommerce", "website_hint": "shopify.dev"},
    {"id": 42, "name": "WooCommerce", "category": "Ecommerce", "website_hint": "woocommerce.com/document/woocommerce-rest-api"},
    {"id": 43, "name": "BigCommerce", "category": "Ecommerce", "website_hint": "developer.bigcommerce.com"},
    {"id": 44, "name": "Salesforce Commerce Cloud", "category": "Ecommerce", "website_hint": "developer.salesforce.com/docs/commerce"},
    {"id": 45, "name": "Magento (Adobe Commerce)", "category": "Ecommerce", "website_hint": "developer.adobe.com/commerce"},
    {"id": 46, "name": "Squarespace", "category": "Ecommerce", "website_hint": "developers.squarespace.com"},
    {"id": 47, "name": "Ecwid", "category": "Ecommerce", "website_hint": "api-docs.ecwid.com"},
    {"id": 48, "name": "Gumroad", "category": "Ecommerce", "website_hint": "gumroad.com/api"},
    {"id": 49, "name": "Amazon Selling Partner", "category": "Ecommerce", "website_hint": "developer-docs.amazon.com/sp-api"},
    {"id": 50, "name": "fanbasis", "category": "Ecommerce", "website_hint": "fanbasis.com"},

    # 6. Data, SEO and Scraping
    {"id": 51, "name": "DataForSEO", "category": "Data, SEO and Scraping", "website_hint": "docs.dataforseo.com"},
    {"id": 52, "name": "SE Ranking", "category": "Data, SEO and Scraping", "website_hint": "seranking.com/api"},
    {"id": 53, "name": "Ahrefs", "category": "Data, SEO and Scraping", "website_hint": "ahrefs.com/api"},
    {"id": 54, "name": "MrScraper", "category": "Data, SEO and Scraping", "website_hint": "docs.mrscraper.com"},
    {"id": 55, "name": "Apify", "category": "Data, SEO and Scraping", "website_hint": "docs.apify.com"},
    {"id": 56, "name": "Firecrawl", "category": "Data, SEO and Scraping", "website_hint": "firecrawl.dev"},
    {"id": 57, "name": "Bright Data", "category": "Data, SEO and Scraping", "website_hint": "brightdata.com"},
    {"id": 58, "name": "Sherlock", "category": "Data, SEO and Scraping", "website_hint": "github.com/sherlock-project/sherlock"},
    {"id": 59, "name": "Waterfall.io", "category": "Data, SEO and Scraping", "website_hint": "waterfall.io (contact/company intel)"},
    {"id": 60, "name": "Clay", "category": "Data, SEO and Scraping", "website_hint": "clay.com"},

    # 7. Developer, Infra and Data platforms
    {"id": 61, "name": "GitHub", "category": "Developer, Infra and Data platforms", "website_hint": "docs.github.com/rest"},
    {"id": 62, "name": "Vercel", "category": "Developer, Infra and Data platforms", "website_hint": "vercel.com/docs/rest-api"},
    {"id": 63, "name": "Netlify", "category": "Developer, Infra and Data platforms", "website_hint": "docs.netlify.com/api"},
    {"id": 64, "name": "Cloudflare", "category": "Developer, Infra and Data platforms", "website_hint": "developers.cloudflare.com/api"},
    {"id": 65, "name": "Supabase", "category": "Developer, Infra and Data platforms", "website_hint": "supabase.com/docs"},
    {"id": 66, "name": "Neo4j", "category": "Developer, Infra and Data platforms", "website_hint": "neo4j.com/docs/api"},
    {"id": 67, "name": "Snowflake", "category": "Developer, Infra and Data platforms", "website_hint": "docs.snowflake.com"},
    {"id": 68, "name": "MongoDB Atlas", "category": "Developer, Infra and Data platforms", "website_hint": "mongodb.com/docs/atlas/api"},
    {"id": 69, "name": "Datadog", "category": "Developer, Infra and Data platforms", "website_hint": "docs.datadoghq.com/api"},
    {"id": 70, "name": "Sentry", "category": "Developer, Infra and Data platforms", "website_hint": "docs.sentry.io/api"},

    # 8. Productivity and Project Management
    {"id": 71, "name": "Notion", "category": "Productivity and Project Management", "website_hint": "developers.notion.com"},
    {"id": 72, "name": "Airtable", "category": "Productivity and Project Management", "website_hint": "airtable.com/developers"},
    {"id": 73, "name": "Linear", "category": "Productivity and Project Management", "website_hint": "developers.linear.app"},
    {"id": 74, "name": "Jira", "category": "Productivity and Project Management", "website_hint": "developer.atlassian.com"},
    {"id": 75, "name": "Asana", "category": "Productivity and Project Management", "website_hint": "developers.asana.com"},
    {"id": 76, "name": "Monday.com", "category": "Productivity and Project Management", "website_hint": "developer.monday.com"},
    {"id": 77, "name": "ClickUp", "category": "Productivity and Project Management", "website_hint": "clickup.com/api"},
    {"id": 78, "name": "Coda", "category": "Productivity and Project Management", "website_hint": "coda.io/developers"},
    {"id": 79, "name": "Smartsheet", "category": "Productivity and Project Management", "website_hint": "smartsheet.com/developers"},
    {"id": 80, "name": "Harvest", "category": "Productivity and Project Management", "website_hint": "harvestapp.com (help.getharvest.com/api-v2)"},

    # 9. Finance and Fintech
    {"id": 81, "name": "Stripe", "category": "Finance and Fintech", "website_hint": "stripe.com/docs/api"},
    {"id": 82, "name": "Plaid", "category": "Finance and Fintech", "website_hint": "plaid.com/docs"},
    {"id": 83, "name": "Binance", "category": "Finance and Fintech", "website_hint": "binance-docs.github.io"},
    {"id": 84, "name": "Paygent Connect", "category": "Finance and Fintech", "website_hint": "paygent (NMI-powered)"},
    {"id": 85, "name": "iPayX", "category": "Finance and Fintech", "website_hint": "ipayx.ai/docs"},
    {"id": 86, "name": "QuickBooks", "category": "Finance and Fintech", "website_hint": "developer.intuit.com"},
    {"id": 87, "name": "Xero", "category": "Finance and Fintech", "website_hint": "developer.xero.com"},
    {"id": 88, "name": "Brex", "category": "Finance and Fintech", "website_hint": "developer.brex.com"},
    {"id": 89, "name": "Ramp", "category": "Finance and Fintech", "website_hint": "docs.ramp.com"},
    {"id": 90, "name": "PitchBook", "category": "Finance and Fintech", "website_hint": "pitchbook.com (research API)"},

    # 10. AI, Research and Media-native
    {"id": 91, "name": "NotebookLM", "category": "AI, Research and Media-native", "website_hint": "cloud.google.com/gemini (Enterprise API)"},
    {"id": 92, "name": "Otter AI", "category": "AI, Research and Media-native", "website_hint": "help.otter.ai (MCP server)"},
    {"id": 93, "name": "Fathom", "category": "AI, Research and Media-native", "website_hint": "fathom.video"},
    {"id": 94, "name": "Consensus", "category": "AI, Research and Media-native", "website_hint": "consensus.app (OAuth requested)"},
    {"id": 95, "name": "Reducto", "category": "AI, Research and Media-native", "website_hint": "reducto.ai (document parsing)"},
    {"id": 96, "name": "Devin", "category": "AI, Research and Media-native", "website_hint": "docs.devin.ai (MCP)"},
    {"id": 97, "name": "higgsfield", "category": "AI, Research and Media-native", "website_hint": "higgsfield.ai/cli (content suite)"},
    {"id": 98, "name": "Mermaid CLI", "category": "AI, Research and Media-native", "website_hint": "github.com/mermaid-js/mermaid-cli"},
    {"id": 99, "name": "YouTube Transcript", "category": "AI, Research and Media-native", "website_hint": "transcriptapi.com"},
    {"id": 100, "name": "Grain", "category": "AI, Research and Media-native", "website_hint": "grain.com (meeting notes)"}
]

