<script lang="ts">
	import { mode } from 'mode-watcher';
	import { themeState } from '$lib/theme-state.svelte';

	let { src, class: className }: { src: string; class?: string } = $props();

	let iframeEl: HTMLIFrameElement | undefined = $state();

	function sendTheme() {
		iframeEl?.contentWindow?.postMessage(
			{ type: 'bramble-theme', theme: themeState.current, mode: mode.current },
			'*'
		);
	}

	// Sync theme + mode to iframe via postMessage for live updates
	$effect(() => {
		// Read reactively so effect re-runs on changes
		const _theme = themeState.current;
		const _mode = mode.current;
		if (iframeEl?.contentWindow) {
			sendTheme();
		}
	});

	// Listen for "ready" handshake from iframe after hydration
	$effect(() => {
		function handleMessage(e: MessageEvent) {
			if (e.data?.type === 'bramble-embed-ready') {
				sendTheme();
			}
		}
		window.addEventListener('message', handleMessage);
		return () => window.removeEventListener('message', handleMessage);
	});

	function handleLoad() {
		sendTheme();
	}
</script>

<div class="device-frame {className ?? ''}" data-component="device-frame">
	<div class="device-bezel" data-component="device-bezel">
		<div class="device-island" data-component="device-island"></div>

		<iframe
			bind:this={iframeEl}
			{src}
			title="Mobile preview"
			class="device-screen"
			onload={handleLoad}
			data-component="device-screen"
		></iframe>

		<div class="device-home-indicator" data-component="device-home-indicator"></div>
	</div>
</div>

<style>
	.device-frame {
		display: flex;
		justify-content: center;
	}

	.device-bezel {
		position: relative;
		width: 399px;
		height: 836px;
		background: oklch(0.15 0 0);
		border-radius: 44px;
		padding: 12px;
		box-shadow:
			0 0 0 1px oklch(0.3 0 0),
			0 0 40px oklch(0.5 0 0 / 0.08),
			0 20px 60px oklch(0 0 0 / 0.3);
	}

	.device-island {
		position: absolute;
		top: 18px;
		left: 50%;
		transform: translateX(-50%);
		width: 120px;
		height: 34px;
		background: oklch(0.1 0 0);
		border-radius: 20px;
		z-index: 10;
	}

	.device-screen {
		width: 375px;
		height: 812px;
		border: none;
		border-radius: 38px;
		overflow: hidden;
	}

	.device-home-indicator {
		position: absolute;
		bottom: 18px;
		left: 50%;
		transform: translateX(-50%);
		width: 134px;
		height: 5px;
		background: oklch(0.4 0 0);
		border-radius: 3px;
	}
</style>
