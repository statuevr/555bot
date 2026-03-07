import discord
from discord.ext import commands
from discord import app_commands

# ─────────────────────────────────────────

# CONFIG — paste your NEW token here

# ─────────────────────────────────────────

BOT_TOKEN   = “MTQ3OTU5OTU3MTA2NjgxNDY2MA.GgsclI.YWdrGBWOB9lgvniWKBrLiZ1lpslXouEKH_Fptc”   # Reset at discord.com/developers/applications
OWNER_ID    = 0                        # Replace with your Discord user ID (number)

# Role name that is allowed to use /warn

WARN_ROLE   = “mod”                    # Change to your exact role name

# ─────────────────────────────────────────

# BOT SETUP

# ─────────────────────────────────────────

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=”!”, intents=intents)
tree = bot.tree

# ─────────────────────────────────────────

# HELPERS

# ─────────────────────────────────────────

def is_owner(interaction: discord.Interaction) -> bool:
return interaction.user.id == OWNER_ID

def has_warn_role(interaction: discord.Interaction) -> bool:
if is_owner(interaction):
return True
return any(r.name.lower() == WARN_ROLE.lower() for r in interaction.user.roles)

# ─────────────────────────────────────────

# /ban  (owner only)

# ─────────────────────────────────────────

@tree.command(name=“ban”, description=“Ban a member from the server.”)
@app_commands.describe(member=“The member to ban”, reason=“Reason for the ban”)
async def ban_cmd(interaction: discord.Interaction, member: discord.Member, reason: str = “No reason provided”):
if not is_owner(interaction):
await interaction.response.send_message(“❌ Only the owner can use this command.”, ephemeral=True)
return
try:
await member.ban(reason=reason)
await interaction.response.send_message(f”🔨 **{member}** has been banned. Reason: {reason}”)
except discord.Forbidden:
await interaction.response.send_message(“❌ I don’t have permission to ban that user.”, ephemeral=True)

# ─────────────────────────────────────────

# /kick  (owner only)

# ─────────────────────────────────────────

@tree.command(name=“kick”, description=“Kick a member from the server.”)
@app_commands.describe(member=“The member to kick”, reason=“Reason for the kick”)
async def kick_cmd(interaction: discord.Interaction, member: discord.Member, reason: str = “No reason provided”):
if not is_owner(interaction):
await interaction.response.send_message(“❌ Only the owner can use this command.”, ephemeral=True)
return
try:
await member.kick(reason=reason)
await interaction.response.send_message(f”👢 **{member}** has been kicked. Reason: {reason}”)
except discord.Forbidden:
await interaction.response.send_message(“❌ I don’t have permission to kick that user.”, ephemeral=True)

# ─────────────────────────────────────────

# /warn  (owner OR warn-role)

# ─────────────────────────────────────────

@tree.command(name=“warn”, description=“Warn a member. Usage: /warn @username reason”)
@app_commands.describe(member=“The member to warn (@username)”, reason=“Reason for the warning”)
async def warn_cmd(interaction: discord.Interaction, member: discord.Member, reason: str = “No reason provided”):
if not has_warn_role(interaction):
await interaction.response.send_message(“❌ You don’t have permission to warn members.”, ephemeral=True)
return
await interaction.response.send_message(
f”⚠️ {member.mention} has been **warned** by {interaction.user.mention}.\n**Reason:** {reason}”
)

# ─────────────────────────────────────────

# /buyer  (owner only — ephemeral buttons)

# ─────────────────────────────────────────

class BuyerView(discord.ui.View):
def **init**(self):
super().**init**(timeout=120)

```
@discord.ui.button(label="Buy", style=discord.ButtonStyle.success)
async def buy_button(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(
        "🛒 **Buy here:** https://555mods.mysellauth.com/product/555-suporter",
        ephemeral=True
    )

@discord.ui.button(label="Redeem", style=discord.ButtonStyle.primary)
async def redeem_button(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message("🔑 Redeem — **Coming Soon!**", ephemeral=True)

@discord.ui.button(label="Robux", style=discord.ButtonStyle.secondary)
async def robux_button(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message("💰 Robux — **Coming Soon!**", ephemeral=True)
```

@tree.command(name=“buyer”, description=“Show buyer options (owner only).”)
async def buyer_cmd(interaction: discord.Interaction):
if not is_owner(interaction):
await interaction.response.send_message(“❌ Only the owner can use this command.”, ephemeral=True)
return
await interaction.response.send_message(
“🛍️ **555 Bot — Buyer Menu**\nOnly you can see this.”,
view=BuyerView(),
ephemeral=True
)

# ─────────────────────────────────────────

# /verified  (coming soon)

# ─────────────────────────────────────────

@tree.command(name=“verified”, description=“Verify your game account.”)
async def verified_cmd(interaction: discord.Interaction):
await interaction.response.send_message(
“✅ **Verification — Coming Soon!**\nThis feature is not ready yet.”,
ephemeral=True
)

# ─────────────────────────────────────────

# ON READY

# ─────────────────────────────────────────

@bot.event
async def on_ready():
await tree.sync()
print(f”✅ 555 Bot is online as {bot.user} (ID: {bot.user.id})”)
print(“Slash commands synced.”)

# ─────────────────────────────────────────

# RUN

# ─────────────────────────────────────────

bot.run(BOT_TOKEN)
