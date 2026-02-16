<script lang="ts">
	import { Button as ShadcnButton, type ButtonProps, buttonVariants } from '$ui/button';

	let { variant = 'default', class: className, ...restProps }: ButtonProps = $props();

	/** Bramble color overrides by variant — keeps shadcn files pristine */
	const overrides: Record<string, string> = {
		default: 'active:bg-primary/80',
		destructive: 'active:bg-destructive/80',
		outline: 'hover:bg-secondary hover:text-secondary-foreground active:bg-secondary/80 dark:hover:bg-input/50 dark:active:bg-input/70',
		secondary: 'active:bg-secondary/70',
		ghost: 'hover:bg-secondary hover:text-secondary-foreground active:bg-secondary/80 dark:hover:bg-accent/50 dark:active:bg-accent/70',
		link: ''
	};
</script>

<ShadcnButton {variant} class="{overrides[variant ?? 'default'] ?? ''} {className ?? ''}" {...restProps} />
