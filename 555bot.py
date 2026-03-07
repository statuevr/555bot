import discord
import os
from discord.ext import commands
from discord import app_commands

BOT_TOKEN = MTQ3OTU5OTU3MTA2NjgxNDY2MA.Go9aO8.N6b3ZZQRyVqiRKV_RLB7_bGgFjHvVXrbbNsg40
OWNER_ID = 1181035571678810256
WARN_ROLE = “mod”

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=”!”, intents=intents)
tree = bot.tree

def is_owner(interaction):
return interaction.user.id == OWNER_ID

def has_warn_role(interaction):
if is_owner(interaction):
return True
return any(r.name.lower() == WARN_ROLE.lower() for r in interaction.user.roles)

@tree.command(name=“ban”, description=“Ban a member from the server.”)
@app_commands.describe(member=“The member to ban”, reason=“Reason for the ban”)
async def ban_cmd(interaction, member: discord.Member, reason: str = “No reason provided”):
if not is_owner(interaction):
await interaction.response.send_message(“Only the owner can use this command.”, ephemeral=True)
return
try:
await member.ban(reason=reason)
await interaction.response.send_message(f”{member} has been banned. Reason: {reason}”)
except discord.Forbidden:
await interaction.response.send_message(“I do not have permission to ban that user.”, ephemeral=True)

@tree.command(name=“kick”, description=“Kick a member from the server.”)
@app_commands.describe(member=“The member to kick”, reason=“Reason for the kick”)
async def kick_cmd(interaction, member: discord.Member, reason: str = “No reason provided”):
if not is_owner(interaction):
await interaction.response.send_message(“Only the owner can use this command.”, ephemeral=True)
return
try:
await member.kick(reason=reason)
await interaction.response.send_message(f”{member} has been kicked. Reason: {reason}”)
except discord.Forbidden:
await interaction.response.send_message(“I do not have permission to kick that user.”, ephemeral=True)

@tree.command(name=“warn”, description=“Warn a member.”)
@app_commands.describe(member=“The member to warn”, reason=“Reason for the warning”)
async def warn_cmd(interaction, member: discord.Member, reason: str = “No reason provided”):
if not has_warn_role(interaction):
await interaction.response.send_message(“You do not have permission to warn members.”, ephemeral=True)
return
await interaction.response.send_message(
f”{member.mention} has been warned by {interaction.user.mention}. Reason: {reason}”
)

class BuyerView(discord.ui.View):
def **init**(self):
super().**init**(timeout=120)

```
@discord.ui.button(label="Buy", style=discord.ButtonStyle.success)
async def buy_button(self, interaction, button: discord.ui.Button):
    await interaction.response.send_message(
        "Buy here: https://555mods.mysellauth.com/product/555-suporter",
        ephemeral=True
    )

@discord.ui.button(label="Redeem", style=discord.ButtonStyle.primary)
async def redeem_button(self, interaction, button: discord.ui.Button):
    await interaction.response.send_message("Redeem - Coming Soon!", ephemeral=True)

@discord.ui.button(label="Robux", style=discord.ButtonStyle.secondary)
async def robux_button(self, interaction, button: discord.ui.Button):
    await interaction.response.send_message("Robux - Coming Soon!", ephemeral=True)
```

@tree.command(name=“buyer”, description=“Show buyer options.”)
async def buyer_cmd(interaction):
if not is_owner(interaction):
await interaction.response.send_message(“Only the owner can use this command.”, ephemeral=True)
return
await interaction.response.send_message(
“555 Bot Buyer Menu - Only you can see this.”,
view=BuyerView(),
ephemeral=True
)

@tree.command(name=“verified”, description=“Verify your game account.”)
async def verified_cmd(interaction):
await interaction.response.send_message(“Verification - Coming Soon!”, ephemeral=True)

@bot.event
async def on_ready():
await tree.sync()
print(f”555 Bot is online as {bot.user}”)

bot.run(os.environ["BOT_TOKEN"])
