#!/usr/bin/env python3
"""
RabtaCar Tag Generator
Generates 100 individual HTML tag pages (RBC-1001 to RBC-1100)
"""

import os

# Configuration
WHATSAPP_NUMBER = "923167772969"
START_TAG = 1001
END_TAG = 1100
OUTPUT_DIR = "tag-pages"

# HTML Template
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="RabtaCar - Smart Vehicle Alert System. Notify vehicle owner instantly without sharing phone numbers.">
    <title>RabtaCar Alert - Tag {tag_id}</title>
    
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #C9FC01 0%, #FFD700 50%, #FFA500 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 15px;
            animation: gradientShift 10s ease infinite;
            background-size: 200% 200%;
        }}
        
        @keyframes gradientShift {{
            0%, 100% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
        }}
        
        .container {{
            background: white;
            border-radius: 24px;
            padding: 35px 30px;
            max-width: 480px;
            width: 100%;
            box-shadow: 0 25px 70px rgba(0,0,0,0.35);
            text-align: center;
            animation: slideUp 0.5s ease-out;
        }}
        
        @keyframes slideUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .header {{
            margin-bottom: 25px;
        }}
        
        .brand-name {{
            font-size: 38px;
            font-weight: 800;
            color: #000;
            margin-bottom: 8px;
        }}
        
        .tagline {{
            font-size: 14px;
            color: #666;
            font-weight: 600;
            margin-bottom: 15px;
        }}
        
        h1 {{
            color: #333;
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 8px;
        }}
        
        .subtitle {{
            color: #666;
            font-size: 14px;
            line-height: 1.5;
        }}
        
        .tag-section {{
            margin: 20px 0;
            padding: 15px;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 12px;
        }}
        
        .tag-id {{
            font-size: 18px;
            color: #000;
            font-weight: 700;
            letter-spacing: 1px;
        }}
        
        .section-title {{
            font-size: 16px;
            font-weight: 700;
            color: #333;
            margin: 25px 0 15px;
            text-align: left;
        }}
        
        .alert-options {{
            margin: 20px 0;
            display: grid;
            gap: 10px;
        }}
        
        .alert-button {{
            display: flex;
            align-items: center;
            width: 100%;
            padding: 16px 18px;
            background: white;
            border: 2px solid #e8e8e8;
            border-radius: 14px;
            font-size: 15px;
            font-weight: 500;
            color: #333;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-align: left;
            position: relative;
            overflow: hidden;
        }}
        
        .alert-button:hover {{
            border-color: #C9FC01;
            background: linear-gradient(135deg, #fffef7 0%, #fff9e6 100%);
            transform: translateX(5px);
            box-shadow: 0 4px 12px rgba(201, 252, 1, 0.3);
        }}
        
        .alert-button.selected {{
            border-color: #C9FC01;
            background: linear-gradient(135deg, #f0ffe6 0%, #e8ffcc 100%);
            box-shadow: 0 4px 16px rgba(201, 252, 1, 0.4);
        }}
        
        .alert-button .icon {{
            margin-right: 14px;
            font-size: 24px;
            min-width: 28px;
            text-align: center;
        }}
        
        .alert-button .text {{
            flex: 1;
        }}
        
        .alert-button .check {{
            opacity: 0;
            color: #C9FC01;
            font-size: 20px;
            transition: opacity 0.3s;
            filter: brightness(0.6);
        }}
        
        .alert-button.selected .check {{
            opacity: 1;
        }}
        
        .whatsapp-container {{
            margin-top: 25px;
            display: none;
            animation: fadeIn 0.4s ease-out;
        }}
        
        @keyframes fadeIn {{
            from {{
                opacity: 0;
                transform: scale(0.95);
            }}
            to {{
                opacity: 1;
                transform: scale(1);
            }}
        }}
        
        .whatsapp-container.show {{
            display: block;
        }}
        
        .selected-issue {{
            background: #f8f9fa;
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 15px;
            font-size: 14px;
            color: #666;
        }}
        
        .selected-issue strong {{
            color: #333;
        }}
        
        .whatsapp-button {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: #25D366;
            color: white;
            padding: 14px 28px;
            border-radius: 50px;
            text-decoration: none;
            font-size: 15px;
            font-weight: 700;
            transition: all 0.3s;
            box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
            border: none;
            cursor: pointer;
            width: 100%;
            flex-direction: column;
            gap: 3px;
        }}
        
        .whatsapp-button:hover {{
            background: #20BA5A;
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(37, 211, 102, 0.5);
        }}
        
        .whatsapp-button .wa-icon {{
            font-size: 20px;
            margin-bottom: 3px;
        }}
        
        .button-text-ur {{
            font-size: 16px;
            font-family: 'Noto Nastaliq Urdu', 'Jameel Noori Nastaleeq', 'Urdu Typesetting', serif;
            direction: rtl;
            line-height: 1.3;
        }}
        
        .button-text-en {{
            font-size: 14px;
            font-weight: 700;
        }}
        
        .footer {{
            margin-top: 30px;
            padding-top: 25px;
            border-top: 1px solid #e8e8e8;
        }}
        
        .privacy-notice {{
            display: flex;
            align-items: center;
            justify-content: center;
            color: #888;
            font-size: 13px;
            margin-bottom: 12px;
        }}
        
        .privacy-notice .lock-icon {{
            color: #C9FC01;
            filter: brightness(0.6);
            margin-right: 6px;
            font-size: 16px;
        }}
        
        .powered-by {{
            color: #bbb;
            font-size: 12px;
        }}
        
        .powered-by a {{
            color: #999;
            text-decoration: none;
            font-weight: 600;
        }}
        
        .powered-by a:hover {{
            color: #C9FC01;
            filter: brightness(0.6);
        }}
        
        @media (max-width: 480px) {{
            .container {{
                padding: 25px 20px;
            }}
            
            .brand-name {{
                font-size: 32px;
            }}
            
            .alert-button {{
                padding: 14px 16px;
                font-size: 14px;
            }}
            
            .alert-button .icon {{
                font-size: 20px;
            }}
            
            .whatsapp-button {{
                padding: 12px 24px;
                font-size: 14px;
            }}
            
            .button-text-ur {{
                font-size: 15px;
            }}
            
            .button-text-en {{
                font-size: 13px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="brand-name">RabtaCar</div>
            <div class="tagline">#GetFoundNow</div>
            <h1>Vehicle Alert System</h1>
            <p class="subtitle">Select an issue to notify the vehicle owner instantly</p>
        </div>
        
        <div class="tag-section">
            <div class="tag-id">Tag ID: {tag_id}</div>
        </div>
        
        <div class="section-title">🚨 Select Issue Type:</div>
        <div class="alert-options">
            <button class="alert-button" onclick="selectIssue('No Parking Zone', '🚫')">
                <span class="icon">🚫</span>
                <span class="text">No Parking Zone</span>
                <span class="check">✓</span>
            </button>
            
            <button class="alert-button" onclick="selectIssue('Vehicle Being Towed', '🚨')">
                <span class="icon">🚨</span>
                <span class="text">Vehicle Being Towed</span>
                <span class="check">✓</span>
            </button>
            
            <button class="alert-button" onclick="selectIssue('Headlights On', '💡')">
                <span class="icon">💡</span>
                <span class="text">Headlights On</span>
                <span class="check">✓</span>
            </button>
            
            <button class="alert-button" onclick="selectIssue('Window/Door Open', '🚪')">
                <span class="icon">🚪</span>
                <span class="text">Window/Door Open</span>
                <span class="check">✓</span>
            </button>
            
            <button class="alert-button" onclick="selectIssue('Emergency Situation', '⚠️')">
                <span class="icon">⚠️</span>
                <span class="text">Emergency Situation</span>
                <span class="check">✓</span>
            </button>
            
            <button class="alert-button" onclick="selectIssue('Other Issue', '📝')">
                <span class="icon">📝</span>
                <span class="text">Other Issue</span>
                <span class="check">✓</span>
            </button>
        </div>
        
        <div class="whatsapp-container" id="whatsappContainer">
            <div class="selected-issue">
                <strong>Selected:</strong> <span id="selectedIssueText"></span>
            </div>
            <a href="#" id="whatsappLink" class="whatsapp-button">
                <span class="wa-icon">📱</span>
                <span class="button-text-ur">مطلع کریں</span>
                <span class="button-text-en">Notify Owner</span>
            </a>
        </div>
        
        <div class="footer">
            <div class="privacy-notice">
                <span class="lock-icon">🔒</span>
                <span>Privacy protected. Numbers never shared.</span>
            </div>
            <div class="powered-by">
                Powered by <a href="/">RabtaCar</a>
            </div>
        </div>
    </div>

    <script>
        const CONFIG = {{
            WHATSAPP_NUMBER: '{whatsapp_number}',
            TAG_ID: '{tag_id}'
        }};
        
        let selectedIssue = null;
        let selectedIcon = null;
        
        function selectIssue(issue, icon) {{
            selectedIssue = issue;
            selectedIcon = icon;
            
            document.querySelectorAll('.alert-button').forEach(btn => {{
                btn.classList.remove('selected');
            }});
            
            event.target.closest('.alert-button').classList.add('selected');
            document.getElementById('selectedIssueText').textContent = icon + ' ' + issue;
            
            generateWhatsAppLink(issue, icon);
            
            const container = document.getElementById('whatsappContainer');
            container.classList.add('show');
            
            setTimeout(() => {{
                container.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
            }}, 100);
        }}
        
        function generateWhatsAppLink(issue, icon) {{
            const message = `Hello RabtaCar, I need to contact the owner of vehicle with Tag: ${{CONFIG.TAG_ID}}\\n\\nIssue: ${{issue}} ${{icon}}`;
            const encodedMessage = encodeURIComponent(message);
            const whatsappUrl = `https://wa.me/${{CONFIG.WHATSAPP_NUMBER}}?text=${{encodedMessage}}`;
            
            document.getElementById('whatsappLink').href = whatsappUrl;
        }}
    </script>
</body>
</html>'''

def generate_tag_pages():
    """Generate 100 individual tag HTML pages"""
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    generated_files = []
    
    for tag_num in range(START_TAG, END_TAG + 1):
        tag_id = f"RBC-{tag_num}"
        filename = f"rbc-{tag_num}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Generate HTML content
        html_content = HTML_TEMPLATE.format(
            tag_id=tag_id,
            whatsapp_number=WHATSAPP_NUMBER
        )
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        generated_files.append(filename)
        
        if tag_num % 10 == 0:
            print(f"Generated {tag_num - START_TAG + 1} files...")
    
    print(f"\n✅ Successfully generated {len(generated_files)} tag pages!")
    print(f"📁 Location: {OUTPUT_DIR}/")
    print(f"📄 Files: rbc-1001.html to rbc-1100.html")
    
    return generated_files

if __name__ == "__main__":
    print("🚀 RabtaCar Tag Generator\n")
    print(f"Generating tags from RBC-{START_TAG} to RBC-{END_TAG}...")
    print(f"WhatsApp: {WHATSAPP_NUMBER}\n")
    
    generate_tag_pages()
    
    print("\n✨ All done! Ready to deploy to Netlify!")
