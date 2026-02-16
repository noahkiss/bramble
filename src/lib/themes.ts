export const themes = [
	{
		id: 'lagoon',
		label: 'Lagoon',
		description: 'Cool, polished, mysterious',
		headingFont: 'Syne',
		bodyFont: 'Inter'
	},
	{
		id: 'meadow',
		label: 'Meadow',
		description: 'Warm, earthy, cozy',
		headingFont: 'Lora',
		bodyFont: 'Nunito Sans'
	}
] as const;

export type ThemeId = (typeof themes)[number]['id'];
