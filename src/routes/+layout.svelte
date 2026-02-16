<script lang="ts">
	import '../app.css';
	import { ModeWatcher, toggleMode, mode } from 'mode-watcher';
	import { themes } from '$lib/themes';
	import { themeState } from '$lib/theme-state.svelte';
	import Button from '$lib/components/Button.svelte';
	import DeviceFrame from '$lib/components/DeviceFrame.svelte';

	let { children, data } = $props();

	let mobileView = $state(false);

	// In embed mode: listen for theme/mode from parent, send ready handshake
	$effect(() => {
		if (!data.isEmbed) return;
		function handleMessage(e: MessageEvent) {
			if (e.data?.type !== 'bramble-theme') return;
			document.documentElement.setAttribute('data-theme', e.data.theme);
			document.documentElement.classList.toggle('dark', e.data.mode === 'dark');
		}
		window.addEventListener('message', handleMessage);
		// Tell parent we're ready to receive theme
		window.parent.postMessage({ type: 'bramble-embed-ready' }, '*');
		return () => window.removeEventListener('message', handleMessage);
	});
</script>

{#if data.isEmbed}
	<div class="embed-shell" data-section="embed-root">
		<!-- Status bar / dynamic island blur overlay -->
		<div class="embed-status-bar" data-component="embed-status-bar"></div>

		<!-- Scrollable content -->
		<div class="embed-content" data-section="content">
			<div class="mx-auto max-w-5xl px-4 py-4">
				{@render children()}
			</div>
		</div>

		<!-- iOS tab bar -->
		<nav class="embed-tab-bar" data-component="embed-tab-bar">
			{#each [
				{ icon: 'solar:home-2-bold', label: 'Home' },
				{ icon: 'solar:pallete-2-bold', label: 'Themes' },
				{ icon: 'solar:widget-bold', label: 'Components' },
				{ icon: 'solar:settings-bold', label: 'Settings' }
			] as tab, i}
				<div class="embed-tab-item" class:embed-tab-active={i === 0}>
					<iconify-icon icon={tab.icon} width="22"></iconify-icon>
					<span class="embed-tab-label">{tab.label}</span>
				</div>
			{/each}
		</nav>
	</div>

	<style>
		.embed-shell {
			display: flex;
			flex-direction: column;
			height: 100vh;
			overflow: hidden;
			background: var(--background);
			color: var(--foreground);
			font-family: var(--font-body);
		}

		/* Frosted glass status bar over the dynamic island area */
		.embed-status-bar {
			position: fixed;
			top: 0;
			left: 0;
			right: 0;
			height: 54px;
			background: oklch(from var(--background) l c h / 0.7);
			-webkit-backdrop-filter: blur(20px) saturate(1.8);
			backdrop-filter: blur(20px) saturate(1.8);
			z-index: 100;
		}

		.embed-content {
			flex: 1;
			overflow-y: auto;
			padding-top: 54px;
			-webkit-overflow-scrolling: touch;
			scrollbar-width: none; /* Firefox */
		}

		.embed-content::-webkit-scrollbar {
			display: none; /* Chrome/Safari */
		}

		/* iOS-style tab bar */
		.embed-tab-bar {
			display: flex;
			justify-content: space-around;
			align-items: center;
			padding: 6px 0;
			padding-bottom: 24px; /* home indicator clearance */
			background: oklch(from var(--card) l c h / 0.8);
			-webkit-backdrop-filter: blur(20px) saturate(1.8);
			backdrop-filter: blur(20px) saturate(1.8);
			border-top: 1px solid var(--border);
		}

		.embed-tab-item {
			display: flex;
			flex-direction: column;
			align-items: center;
			gap: 2px;
			padding: 4px 12px;
			color: var(--muted-foreground);
			cursor: default;
		}

		.embed-tab-active {
			color: var(--primary);
		}

		.embed-tab-label {
			font-size: 10px;
			font-family: var(--font-body);
		}
	</style>
{:else}
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
							variant={themeState.current === theme.id ? 'default' : 'outline'}
							size="sm"
							onclick={() => themeState.set(theme.id)}
						>
							{theme.label}
						</Button>
					{/each}

					<div class="mx-2 h-6 w-px bg-border"></div>

					<Button variant="ghost" size="sm" onclick={toggleMode}>
						{#if mode.current === 'dark'}
							<iconify-icon icon="solar:sun-bold" width="18"></iconify-icon>
						{:else}
							<iconify-icon icon="solar:moon-bold" width="18"></iconify-icon>
						{/if}
					</Button>

					<div class="mx-2 hidden h-6 w-px bg-border md:block"></div>

					<Button
						variant={mobileView ? 'default' : 'ghost'}
						size="sm"
						class="hidden md:inline-flex"
						onclick={() => (mobileView = !mobileView)}
						data-action="toggle-mobile-view"
					>
						{#if mobileView}
							<iconify-icon icon="solar:monitor-bold" width="18"></iconify-icon>
						{:else}
							<iconify-icon icon="solar:smartphone-bold" width="18"></iconify-icon>
						{/if}
					</Button>
				</nav>
			</div>
		</header>

		{#if mobileView}
			<div class="mobile-preview-bg" data-section="mobile-preview">
				<DeviceFrame src="/?embed=true" />
			</div>
		{:else}
			<main class="mx-auto max-w-5xl px-6 py-8" data-section="content">
				{@render children()}
			</main>
		{/if}

		<footer class="border-t border-border py-6 text-center text-sm text-muted-foreground">
			Bramble &middot; design system &middot; brand guide
		</footer>
	</div>

	<style>
		/* Offset background when showing mobile preview so the dark
		   device frame doesn't blend into the page background */
		.mobile-preview-bg {
			display: flex;
			justify-content: center;
			align-items: flex-start;
			padding: 2rem 1.5rem;
			min-height: calc(100vh - 130px);
			background:
				radial-gradient(ellipse at center top, oklch(from var(--primary) l c h / 0.04) 0%, transparent 70%);
		}
	</style>
{/if}
