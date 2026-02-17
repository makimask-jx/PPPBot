import discord

async def my_context_menu(interaction: discord.Interaction, message: discord.Message):
	await interaction.response.send_message("Context menu action " + message.author.mention, ephemeral=True)

module = {
	"type": "context_menu",
	"name": "Context Menu Interaction",
	"callback": my_context_menu
}
