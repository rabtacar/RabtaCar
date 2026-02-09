# 📋 Customer Activation Workflow

## When You Receive an Order

This guide shows you exactly how to activate a tag when a customer purchases.

---

## 📝 Example Order

**Customer Details:**
- Name: Ali Khan
- City: Lahore
- Vehicle: Honda Civic 2020
- Vehicle Number: LES-5678
- Phone: +92 300 1234567
- Tag Purchased: RBC-1015
- Price Paid: Rs. 1,200 (Pack of 2)
- Second Tag: RBC-1016

---

## Step-by-Step Activation

### Step 1: Record Order Details

Create a simple order tracking sheet (or use notebook):

```
Order #001
Date: Feb 3, 2026
Customer: Ali Khan
Tags: RBC-1015, RBC-1016
Vehicle 1: LES-5678 (Honda Civic)
Vehicle 2: [Customer will provide later]
Phone: 923001234567
Status: Shipped
```

### Step 2: Open Google Sheets

Go to your **RabtaCar Database** Google Sheet.

### Step 3: Activate Tag in `tags` Sheet

**Find Row for RBC-1015:**

Before:
| TagID | Name | Status | OwnerID |
|-------|------|--------|---------|
| RBC-1015 | | inactive | |

After:
| TagID | Name | Status | OwnerID |
|-------|------|--------|---------|
| RBC-1015 | Ali - Honda Civic | **active** | **O-015** |

**Changes Made:**
1. Name: Add `Ali - Honda Civic` (or just vehicle name)
2. Status: Change `inactive` to `active`
3. OwnerID: Add `O-015` (use O-XXX format, increment for each new customer)

**Repeat for RBC-1016** (if customer provided 2nd vehicle):
| TagID | Name | Status | OwnerID |
|-------|------|--------|---------|
| RBC-1016 | Ali - Mehran | active | O-015 |

*(Same OwnerID because same customer)*

### Step 4: Add Customer to `owners` Sheet

**Add New Row:**

| OwnerID | Phone | Active |
|---------|-------|--------|
| O-015 | 923001234567 | yes |

**Important:**
- OwnerID must match what you entered in `tags` sheet
- Phone format: 923001234567 (country code, no +, no spaces)
- Active: Always `yes` for new customers

### Step 5: Test the Tag

**Test Process:**

1. Go to: `https://your-site.netlify.app/tag-pages/rbc-1015.html`
2. Click any issue (e.g., "No Parking Zone")
3. Click "Notify Owner"
4. WhatsApp should open with pre-filled message
5. Send the message
6. Your MacroDroid should intercept it
7. Customer should receive SMS within 2-5 minutes

**Expected SMS:**
```
RabtaCar Alert! 🚨 
Immediate attention required for your vehicle 
(Tag: RBC-1015). Please check. 
- RabtaCar Team
```

### Step 6: Confirm with Customer

Send WhatsApp message:

```
✅ Great news!

Your RabtaCar tag RBC-1015 is now active and ready to use!

Your vehicle (LES-5678) is now protected.

If anyone scans your tag, you'll get instant SMS alerts on: 0300 1234567

Test it yourself: [your-site.netlify.app/tag-pages/rbc-1015.html]

Need help? Reply anytime!

#GetFoundNow 🚗
```

---

## 🔄 Daily Workflow

### Morning Routine:

1. **Check WhatsApp Orders**
   - New orders overnight?
   - Note tag IDs and details

2. **Check Google Sheets - Alerts Log**
   - Any alerts received?
   - Any errors/issues?
   - Customer satisfaction?

3. **Activate New Tags**
   - Follow steps above for each new order
   - Test each activation
   - Confirm with customers

### Throughout Day:

- Respond to customer questions
- Ship physical tags (TCS/Leopards)
- Update order statuses
- Monitor system health

### Evening Review:

- Count: How many tags activated today?
- Count: How many alerts processed?
- Review: Any system issues?
- Plan: Tomorrow's tasks

---

## 📊 Tracking Sheet Template

Create a simple Google Sheet for order tracking:

| Order# | Date | Customer | Phone | Tags | Vehicle | Status | Notes |
|--------|------|----------|-------|------|---------|--------|-------|
| 001 | Feb 3 | Ali Khan | 923001234567 | RBC-1015, 1016 | LES-5678 | Shipped | Paid Rs. 1200 |
| 002 | Feb 4 | Sara Ahmed | 923211234567 | RBC-1020 | KHI-9012 | Active | Single tag |
| 003 | Feb 5 | Usman Ali | 923121234567 | RBC-1025, 1026 | ICT-3456 | Pending | COD order |

**Status Types:**
- Pending: Order received, not shipped
- Shipped: Tag sent via courier
- Active: Tag activated in system
- Completed: Customer confirmed working

---

## ❌ Deactivating a Tag

### When to Deactivate:

- Customer requests refund
- Tag reported lost/stolen
- Customer wants to transfer to new vehicle
- Subscription ended (if you add this feature later)

### How to Deactivate:

**In `tags` sheet, change Status:**

Before:
| TagID | Name | Status | OwnerID |
|-------|------|--------|---------|
| RBC-1015 | Ali - Civic | active | O-015 |

After:
| TagID | Name | Status | OwnerID |
|-------|------|--------|---------|
| RBC-1015 | Ali - Civic | **inactive** | O-015 |

**That's it!** Tag will stop accepting alerts immediately.

**Note:** Don't delete rows, just change status. Keeps history intact.

---

## 🔄 Transferring a Tag

### Scenario: Customer sells vehicle, new owner wants to use same tag

**Old Owner:** Ali (O-015), Tag RBC-1015  
**New Owner:** Hassan (new), Phone 923451234567

**Steps:**

1. **Deactivate old assignment** (change Status to inactive)
2. **Create new OwnerID** (O-087)
3. **Add new owner to `owners` sheet:**
   | OwnerID | Phone | Active |
   |---------|-------|--------|
   | O-087 | 923451234567 | yes |

4. **Update tag in `tags` sheet:**
   | TagID | Name | Status | OwnerID |
   |-------|------|--------|---------|
   | RBC-1015 | Hassan - Civic | active | **O-087** |

5. **Test and confirm**

---

## 🆘 Common Issues & Solutions

### Issue: "Tag not found or inactive"

**Cause:** Tag status is `inactive` in sheets  
**Solution:** Change Status to `active`

### Issue: Customer not receiving SMS

**Possible Causes:**
1. Phone number wrong in `owners` sheet → Fix phone number
2. OwnerID mismatch between sheets → Verify OwnerID matches
3. Pushbullet offline → Check your phone/device
4. MacroDroid not running → Restart MacroDroid

**Debug Steps:**
1. Check `Alerts` sheet - was alert logged?
2. Check `tags` sheet - is tag active?
3. Check `owners` sheet - is phone correct?
4. Test Pushbullet manually

### Issue: Multiple SMS for one alert

**Cause:** Rate limiting not working  
**Solution:** Check `rate_limit` sheet, ensure 10-min cooldown

---

## 📈 Optimization Tips

### Batch Activation

If you get 10 orders in one day:

1. Collect all order details first
2. Update Google Sheets in batches
3. Test 2-3 random tags (not all 10)
4. Confirm with all customers

### Customer Verification

Before activation, verify:
- ✅ Payment received
- ✅ Phone number confirmed
- ✅ Vehicle number valid format
- ✅ Customer understands how it works

### Template Messages

Save these in WhatsApp:

**Activation Confirmation:**
```
✅ Your RabtaCar tag [TAG_ID] is now active!
Vehicle: [VEHICLE_NUMBER]
You'll receive SMS alerts on: [PHONE]
Test link: [URL]
```

**Troubleshooting:**
```
Let me check your tag status...
What issue are you experiencing?
1. Not receiving alerts
2. Tag QR not scanning
3. Other issue
```

---

## ✅ Quality Checklist

Before marking tag as "Active":

- [ ] Tag ID correct (RBC-XXXX format)
- [ ] Status changed to `active`
- [ ] OwnerID assigned (O-XXX format)
- [ ] Owner added to `owners` sheet
- [ ] Phone number verified (923XXXXXXXX format)
- [ ] Test alert sent successfully
- [ ] Customer confirmed receipt
- [ ] Physical tag shipped (if applicable)

---

## 🎯 Success Metrics

Track these weekly:

**Activation Metrics:**
- Tags activated this week: ___
- Total active tags: ___
- Activation success rate: ___% 

**Performance Metrics:**
- Alerts received: ___
- Average response time: ___ minutes
- Customer satisfaction: ___% 

**Business Metrics:**
- Revenue this week: Rs. ___
- Average order value: Rs. ___
- Repeat customers: ___

---

**This workflow ensures every customer activation is smooth, tested, and tracked!**

**Keep this guide handy and refer to it for each new order.** 📋✅
