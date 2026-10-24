CYAN, RED, GREEN, ORANGE, PURPLE, GREY = "#00d4ff", "#ff6b6b", "#a8ff78", "#ffb86b", "#a78bfa", "#8a91a0"

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;600&display=swap');
:root{--bg:#0a0c0f;--bg2:#111318;--bg3:#181c22;--border:#1f2530;--border2:#2a3040;
--accent:#00d4ff;--red:#ff6b6b;--green:#a8ff78;--text:#e8eaf0;--text2:#8a91a0;--text3:#4a5060;}
.stApp, .stApp input, .stApp button, .stApp label, .stApp p {font-family:'IBM Plex Mono',monospace;}
.stApp {background:var(--bg);}
header[data-testid="stHeader"] {background:transparent;}
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
