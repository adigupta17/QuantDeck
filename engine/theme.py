CYAN, RED, GREEN, ORANGE, PURPLE, GREY = "#00d4ff", "#ff6b6b", "#a8ff78", "#ffb86b", "#a78bfa", "#8a91a0"

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;600&display=swap');
:root{--bg:#0a0c0f;--bg2:#111318;--bg3:#181c22;--border:#1f2530;--border2:#2a3040;
--accent:#00d4ff;--red:#ff6b6b;--green:#a8ff78;--text:#e8eaf0;--text2:#8a91a0;--text3:#4a5060;}
.stApp, .stApp input, .stApp button, .stApp label, .stApp p {font-family:'IBM Plex Mono',monospace;}
.stApp {background:var(--bg);}
header[data-testid="stHeader"] {background:transparent;}
#MainMenu, footer {visibility:hidden;}
.block-container {padding:1.2rem 1.6rem 2rem; max-width:100%;}
[data-testid="stSidebar"] {background:var(--bg2); border-right:1px solid var(--border);}
[data-testid="stSidebar"] .block-container, [data-testid="stSidebarUserContent"] {padding-top:1rem;}
[data-testid="stWidgetLabel"] p {font-size:.72rem; color:var(--text2);}
[data-baseweb="input"], [data-baseweb="select"] > div, [data-baseweb="base-input"] {
  background:var(--bg3) !important; border-color:var(--border2) !important; border-radius:2px !important;}
[data-testid="stSliderThumbValue"], [data-testid="stThumbValue"] {color:var(--accent) !important; font-size:.75rem;}
[data-testid="stSliderTickBarMin"], [data-testid="stSliderTickBarMax"] {color:var(--text3) !important;}
[data-testid="stVerticalBlockBorderWrapper"] {background:var(--bg2); border:1px solid var(--border) !important; border-radius:2px;}
.sec {font-size:.65rem; letter-spacing:.14em; color:var(--text3); text-transform:uppercase;
  border-bottom:1px solid var(--border); padding-bottom:.35rem; margin:1.2rem 0 .7rem;}
</style>
"""

def style(fig, height=300):
    
    fig.update_layout(
        height=height, margin=dict(l=4, r=4, t=26, b=4), hovermode="x unified",
        paper_bgcolor="rgba(0,0,0,0)", 
    )
    ax = dict(gridcolor="#1f2530", zerolinecolor="#2a3040", linecolor="#1f2530",
              tickfont=dict(color="#4a5060"), automargin=True)
    fig.update_xaxes(**ax)
    fig.update_yaxes(**ax)
    return fig
