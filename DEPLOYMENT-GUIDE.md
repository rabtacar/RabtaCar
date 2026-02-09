# 🚀 RabtaCar Complete Deployment Guide

## 📦 Package Contents

This package contains everything you need to launch RabtaCar:

```
rabtacar-project/
├── index.html                  # Landing page (main website)
├── tag-pages/                  # 100 individual tag HTML files
│   ├── rbc-1001.html
│   ├── rbc-1002.html
│   ├── ...
│   └── rbc-1100.html
├── google-sheets-import/       # CSV files for Google Sheets
│   ├── sheet1-tags.csv
│   ├── sheet2-owners.csv
│   ├── sheet3-rate_limit.csv
│   └── sheet4-Alerts.csv
├── netlify.toml                # Netlify configuration
└── DEPLOYMENT-GUIDE.md         # This file
```

---

## 🌐 Part 1: Deploy to Netlify (5 Minutes)

### Step 1: Prepare Files

1. Download the entire `rabtacar-project` folder
2. Make sure all files are present (100 tag pages + index.html)

### Step 2: Deploy to Netlify

**Option A: Netlify Drop (Easiest - No Account)**

1. Go to: https://app.netlify.com/drop
2. Drag the ENTIRE `rabtacar-project` folder onto the page
3. Wait 10-30 seconds
4. Copy the URL (e.g., `https://rabtacar-abc123.netlify.app`)

**Option B: Netlify with Account (Recommended)**

1. Create free account at: https://netlify.com
2. Click "Add new site" → "Deploy manually"
3. Drag the `rabtacar-project` folder
4. Wait for deployment
5. Your site is live!

### Step 3: Test Your Deployment

Visit these URLs and confirm they work:

- Landing page: `https://your-site.netlify.app/`
- Tag page example: `https://your-site.netlify.app/tag-pages/rbc-1001.html`
- Another tag: `https://your-site.netlify.app/tag-pages/rbc-1050.html`

**✅ If all 3 URLs work, deployment successful!**

---

## 📊 Part 2: Setup Google Sheets Database (10 Minutes)

### Step 1: Create New Google Sheet

1. Go to: https://sheets.google.com
2. Click "+ Blank" to create new spreadsheet
3. Rename it to: **RabtaCar Database**

### Step 2: Import CSV Files

**Import Sheet 1 (tags):**

1. File → Import → Upload
2. Select `sheet1-tags.csv`
3. Import location: "Replace current sheet"
4. Click "Import data"
5. Rename this sheet to: **tags**

**Add Sheet 2 (owners):**

1. Click "+" at bottom to add new sheet
2. Rename to: **owners**
3. File → Import → Upload
4. Select `sheet2-owners.csv`
5. Import location: "Replace current sheet"
6. Click "Import data"

**Add Sheet 3 (rate_limit):**

1. Click "+" to add new sheet
2. Rename to: **rate_limit**
3. Import `sheet3-rate_limit.csv`

**Add Sheet 4 (Alerts):**

1. Click "+" to add new sheet
2. Rename to: **Alerts**
3. Import `sheet4-Alerts.csv`

### Step 3: Verify Sheet Structure

**Check that you have 4 sheets:**

✅ **tags** - 100 rows (RBC-1001 to RBC-1100), all "inactive"  
✅ **owners** - Empty (headers only)  
✅ **rate_limit** - Empty (headers only)  
✅ **Alerts** - Empty (headers only)

---

## 🤖 Part 3: Setup Google Apps Script (15 Minutes)

### Step 1: Open Apps Script

1. In your Google Sheet, click: Extensions → Apps Script
2. Delete the default code
3. Paste your existing Google Apps Script code
4. Make sure it has these lines at the top:

```javascript
const PUSHBULLET_TOKEN = "o.hmMis9WMI3CtncUfBjSPrlb6F82tjIhO";
const DEVICE_ID = "ujwSaMl5xgisjDRAilcHue";
```

### Step 2: Deploy as Web App

1. Click "Deploy" → "New deployment"
2. Type: "Web app"
3. Description: "RabtaCar Alert System"
4. Execute as: "Me"
5. Who has access: "Anyone"
6. Click "Deploy"
7. **Copy the Web App URL** (save this!)

Example: `https://script.google.com/macros/s/AKfycby.../exec`

---

## 📱 Part 4: Update MacroDroid (5 Minutes)

### Update HTTP Request URL

1. Open MacroDroid app
2. Edit your RabtaCar macro
3. Find "HTTP Request" action
4. Update URL to your new Apps Script Web App URL
5. Test: Send a test message to trigger the flow

---

## 🏷️ Part 5: Activate Your First Tag (Example)

### When Customer Buys RBC-1001:

**Customer Info:**
- Name: Ali
- Vehicle: LES-5678 (Honda Civic)
- Phone: 923001234567
- Tag: RBC-1001

**Step 1: Update Google Sheets**

Go to **tags** sheet, find row with RBC-1001:

| TagID | Name | Status | OwnerID |
|-------|------|--------|---------|
| RBC-1001 | Honda Civic | **active** | **O-001** |

Change:
- Status: `inactive` → `active`
- OwnerID: (empty) → `O-001`
- Name: (empty) → `Honda Civic` (optional)

**Step 2: Add to owners sheet**

| OwnerID | Phone | Active |
|---------|-------|--------|
| **O-001** | **923001234567** | **yes** |

**Step 3: Test!**

1. Have someone scan the QR code for RBC-1001
2. They select an issue
3. Message goes to your WhatsApp
4. MacroDroid processes it
5. Owner gets SMS via Pushbullet

✅ **If SMS arrives, system is working!**

---

## 🎨 Part 6: Generate QR Codes (For Printing)

You need unique QR codes for each tag.

### Option 1: Online QR Generator

For each tag (RBC-1001 to RBC-1100):

1. Go to: https://www.qr-code-generator.com/
2. URL: `https://your-site.netlify.app/tag-pages/rbc-1001.html`
3. Settings:
   - Size: 600x600px or larger
   - Error correction: High (30%)
   - Format: PNG
4. Download and name: `qr-rbc-1001.png`
5. Repeat for all 100 tags

**Note:** This is manual but ensures quality.

### Option 2: Bulk QR Generator (Python Script)

If you have Python installed:

```bash
pip install qrcode[pil]
python generate_qr_codes.py
```

(Script can be provided if needed)

---

## 📋 Part 7: Daily Operations

### When Customer Orders:

**Order Received:**
1. Note: Tag ID, customer name, phone, vehicle
2. Send tag to customer (via TCS/Leopards)
3. Update Google Sheets (activate tag)
4. Confirm activation with customer

### Managing Tags:

**Check Tag Status:**
- Open Google Sheets → `tags` sheet
- Search for Tag ID
- View: Status, Owner, Last alert time

**Deactivate Tag:**
- Change Status from `active` to `inactive`
- Tag will stop accepting alerts

**View Alert History:**
- Open `Alerts` sheet
- See all alerts received
- Filter by TagID, date, or status

---

## 🔧 Troubleshooting

### Issue: Tag page shows 404

**Solution:**
- Check file name matches: `rbc-1001.html` (lowercase)
- Verify URL: `/tag-pages/rbc-1001.html`
- Redeploy to Netlify

### Issue: WhatsApp not opening

**Solution:**
- Check WhatsApp number in HTML: `923167772969`
- Test on different phone (Android vs iPhone)
- Verify WhatsApp is installed

### Issue: Owner not receiving SMS

**Solution:**
- Check Google Sheets: Tag is `active`?
- Check `owners` sheet: Phone correct?
- Check MacroDroid: Is it running?
- Check Pushbullet: Device online?
- Check `Alerts` sheet: Was request logged?

### Issue: Alerts log shows "Tag not found"

**Solution:**
- Tag might be `inactive` in sheets
- Change Status to `active`
- Ensure OwnerID is filled

---

## 📊 Analytics & Monitoring

### Track Performance:

**Daily Checks:**
- `Alerts` sheet: How many alerts received?
- Most common alert types?
- Which tags are most active?

**Weekly Review:**
- Total active tags (count `active` in tags sheet)
- Alert response rate
- Customer satisfaction

---

## 🚀 Scaling Up

### Adding More Tags (RBC-1101+):

**Step 1:** Create new HTML files
- Copy `rbc-1100.html`
- Rename to `rbc-1101.html`
- Change Tag ID in code: `RBC-1101`

**Step 2:** Add to Google Sheets
- New row in `tags` sheet
- TagID: `RBC-1101`
- Status: `inactive`

**Step 3:** Redeploy to Netlify
- Upload new files to your Netlify site

---

## 🎯 Next Steps

### Immediate (Week 1):
- [ ] Deploy to Netlify
- [ ] Setup Google Sheets
- [ ] Test with 1-2 tags
- [ ] Activate first customer tag

### Short-term (Month 1):
- [ ] Print 50 tags with QR codes
- [ ] Distribute to friends/family
- [ ] Collect feedback
- [ ] Refine process

### Medium-term (Month 2-3):
- [ ] Order 100 professional tags
- [ ] Launch social media (Facebook/Instagram)
- [ ] Start selling (target 50 sales)
- [ ] Custom domain (rabtacar.pk)

### Long-term (Month 6+):
- [ ] WhatsApp Business API
- [ ] Mobile app development
- [ ] Expand to more cities
- [ ] Scale to 1000+ tags

---

## 📞 Support

**Need Help?**

If you encounter any issues:

1. Check this guide's Troubleshooting section
2. Review the error in `Alerts` sheet (Google Sheets)
3. Test each component individually:
   - Netlify site working?
   - Google Sheets accessible?
   - MacroDroid running?
   - Pushbullet connected?

---

## ✅ Launch Checklist

Before going live, verify:

- [ ] Landing page loads correctly
- [ ] All 100 tag pages accessible
- [ ] Google Sheets has 4 sheets (tags, owners, rate_limit, Alerts)
- [ ] Apps Script deployed as Web App
- [ ] MacroDroid pointing to correct Apps Script URL
- [ ] Pushbullet configured and online
- [ ] WhatsApp number correct (923167772969)
- [ ] Test alert works end-to-end
- [ ] QR codes generated for first 10 tags
- [ ] First tag activated in Google Sheets
- [ ] SMS received when test tag scanned

---

## 🎉 You're Ready!

Everything is set up. Now you can:

1. Print your first batch of tags
2. Start selling to customers
3. Activate tags as orders come in
4. Monitor via Google Sheets
5. Scale up gradually

**Good luck with your RabtaCar launch!** 🚀

---

**Version:** 1.0  
**Last Updated:** February 2026  
**Created for:** RabtaCar MVP Launch
