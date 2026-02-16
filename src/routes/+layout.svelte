<script lang="ts">
	import '../app.css';
	import { ModeWatcher, toggleMode, mode } from 'mode-watcher';
	import { themes, type ThemeId } from '$lib/themes';
	import { Button } from '$ui/button';

	let { children } = $props();

	let currentTheme = $state<ThemeId>('catppuccin');

	function setTheme(id: ThemeId) {
		currentTheme = id;
		document.documentElement.setAttribute('data-theme', id);
		localStorage.setItem('bramble-theme', id);
	}

	$effect(() => {
		const saved = localStorage.getItem('bramble-theme') as ThemeId | null;
		if (saved && themes.some((t) => t.id === saved)) {
			currentTheme = saved;
			document.documentElement.setAttribute('data-theme', saved);
		}
	});
</script>

<ModeWatcher />

<div class="min-h-screen bg-background text-foreground" data-section="root">
	<header class="border-b border-border bg-card" data-component="site-header">
		<div class="mx-auto flex max-w-5xl items-center justify-between px-6 py-4">
			<div class="flex items-center gap-3">
				<h1 class="text-xl font-bold tracking-tight">Bramble</h1>
				<span class="text-sm text-muted-foreground">design system</span>
			</div>

			<nav class="flex items-center gap-2" data-component="theme-controls">
				{#each themes as theme}
					<Button
						variant={currentTheme === theme.id ? 'default' : 'outline'}
						size="sm"
						onclick={() => setTheme(theme.id)}
					>
						{theme.label}
					</Button>
				{/each}

				<div class="mx-2 h-6 w-px bg-border"></div>

				<Button variant="ghost" size="sm" onclick={toggleMode}>
					{#if $mode === 'dark'}
						<iconify-icon icon="solar:sun-bold" width="18"></iconify-icon>
					{:else}
						<iconify-icon icon="solar:moon-bold" width="18"></iconify-icon>
					{/if}
				</Button>
			</nav>
		</div>
	</header>

	<main class="mx-auto max-w-5xl px-6 py-8" data-section="content">
		{@render children()}
	</main>

	<footer class="border-t border-border py-6 text-center text-sm text-muted-foreground">
		Bramble &middot; design system &middot; brand guide
	</footer>
</div>
