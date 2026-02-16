import type { ThemeId } from '$lib/themes';

let current = $state<ThemeId>('lagoon');

export const themeState = {
	get current() {
		return current;
	},
	set(id: ThemeId) {
		current = id;
		document.documentElement.setAttribute('data-theme', id);
	}
};
