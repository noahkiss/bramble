<script lang="ts">
	import { Toggle as ShadcnToggle } from '$ui/toggle';
	import type { Toggle as TogglePrimitive } from 'bits-ui';
	import type { ToggleVariant, ToggleSize } from '$ui/toggle/toggle.svelte';

	let {
		variant = 'default',
		pressed = $bindable(false),
		class: className,
		...restProps
	}: TogglePrimitive.RootProps & {
		variant?: ToggleVariant;
		size?: ToggleSize;
	} = $props();

	/** Bramble overrides: readable hover, primary pressed state */
	const overrides: Record<string, string> = {
		default: 'data-[state=on]:bg-primary/15 data-[state=on]:text-primary',
		outline: 'hover:bg-secondary hover:text-secondary-foreground data-[state=on]:bg-primary/15 data-[state=on]:text-primary'
	};
</script>

<ShadcnToggle {variant} bind:pressed class="{overrides[variant ?? 'default'] ?? ''} {className ?? ''}" {...restProps} />
