export const themes = [
	{
		id: 'catppuccin',
		label: 'Catppuccin',
		description: 'Clean, polished, professional',
		headingFont: 'Syne',
		bodyFont: 'Inter'
	},
	{
		id: 'desert',
		label: 'Desert',
		description: 'Warm, earthy, cozy',
		headingFont: 'Lora',
		bodyFont: 'Nunito Sans'
	}
] as const;

export type ThemeId = (typeof themes)[number]['id'];
