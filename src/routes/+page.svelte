<script lang="ts">
	import { Button } from '$ui/button';
	import * as Card from '$ui/card';
	import { Badge } from '$ui/badge';
	import { Separator } from '$ui/separator';
	import * as Tabs from '$ui/tabs';
</script>

<svelte:head>
	<title>Bramble — Design System</title>
</svelte:head>

<div class="space-y-12" data-section="showcase">
	<!-- Hero -->
	<section class="space-y-2" data-section="hero">
		<h2 class="text-3xl font-bold tracking-tight">Component Showcase</h2>
		<p class="max-w-2xl text-muted-foreground">
			Switch themes and modes using the controls above. Every component on this page
			updates instantly — same markup, different personality.
		</p>
	</section>

	<Separator.Root />

	<!-- Colors -->
	<section class="space-y-4" data-section="colors">
		<h3 class="text-xl font-semibold">Colors</h3>
		<div class="grid grid-cols-2 gap-3 sm:grid-cols-4 md:grid-cols-6">
			{#each [
				{ name: 'Primary', bg: 'bg-primary', fg: 'text-primary-foreground' },
				{ name: 'Secondary', bg: 'bg-secondary', fg: 'text-secondary-foreground' },
				{ name: 'Accent', bg: 'bg-accent', fg: 'text-accent-foreground' },
				{ name: 'Muted', bg: 'bg-muted', fg: 'text-muted-foreground' },
				{ name: 'Destructive', bg: 'bg-destructive', fg: 'text-white' },
				{ name: 'Card', bg: 'bg-card', fg: 'text-card-foreground' }
			] as swatch}
				<div
					class="flex h-20 items-end rounded-lg border border-border p-2 {swatch.bg}"
					data-component="color-swatch"
				>
					<span class="text-xs font-medium {swatch.fg}">{swatch.name}</span>
				</div>
			{/each}
		</div>
	</section>

	<Separator.Root />

	<!-- Typography -->
	<section class="space-y-4" data-section="typography">
		<h3 class="text-xl font-semibold">Typography</h3>
		<div class="space-y-3">
			<p class="font-serif text-3xl font-bold">Heading Font (font-serif)</p>
			<p class="text-lg">Body text uses the theme's body font. This paragraph demonstrates
				the default reading experience — line height, letter spacing, and overall rhythm.
				Good typography is invisible; you just read.</p>
			<p class="font-mono text-sm text-muted-foreground">
				Monospace: const bramble = "design system";
			</p>
		</div>
	</section>

	<Separator.Root />

	<!-- Buttons -->
	<section class="space-y-4" data-section="buttons">
		<h3 class="text-xl font-semibold">Buttons</h3>
		<div class="flex flex-wrap gap-3">
			<Button>Primary</Button>
			<Button variant="secondary">Secondary</Button>
			<Button variant="outline">Outline</Button>
			<Button variant="ghost">Ghost</Button>
			<Button variant="destructive">Destructive</Button>
			<Button variant="link">Link</Button>
		</div>
		<div class="flex flex-wrap gap-3">
			<Button size="sm">Small</Button>
			<Button size="default">Default</Button>
			<Button size="lg">Large</Button>
		</div>
	</section>

	<Separator.Root />

	<!-- Badges -->
	<section class="space-y-4" data-section="badges">
		<h3 class="text-xl font-semibold">Badges</h3>
		<div class="flex flex-wrap gap-2">
			<Badge>Default</Badge>
			<Badge variant="secondary">Secondary</Badge>
			<Badge variant="outline">Outline</Badge>
			<Badge variant="destructive">Destructive</Badge>
		</div>
	</section>

	<Separator.Root />

	<!-- Cards -->
	<section class="space-y-4" data-section="cards">
		<h3 class="text-xl font-semibold">Cards</h3>
		<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
			<Card.Root data-component="feature-card">
				<Card.Header>
					<Card.Title>TinyLedger</Card.Title>
					<Card.Description>Personal bookkeeping for freelancers</Card.Description>
				</Card.Header>
				<Card.Content>
					<p class="text-sm text-muted-foreground">
						Track income, expenses, and taxes. Penny's nerdy look — glasses and bowtie.
					</p>
				</Card.Content>
			</Card.Root>

			<Card.Root data-component="feature-card">
				<Card.Header>
					<Card.Title>Cleaver Manor</Card.Title>
					<Card.Description>Personal life operating system</Card.Description>
				</Card.Header>
				<Card.Content>
					<p class="text-sm text-muted-foreground">
						Home management, routines, and family tools. Penny's cozy look — scarf and mug.
					</p>
				</Card.Content>
			</Card.Root>

			<Card.Root data-component="feature-card">
				<Card.Header>
					<Card.Title>Bramble</Card.Title>
					<Card.Description>Design system &amp; brand guide</Card.Description>
				</Card.Header>
				<Card.Content>
					<p class="text-sm text-muted-foreground">
						You're looking at it. The source of truth for how everything looks and feels.
					</p>
				</Card.Content>
			</Card.Root>
		</div>
	</section>

	<Separator.Root />

	<!-- Tabs -->
	<section class="space-y-4" data-section="tabs">
		<h3 class="text-xl font-semibold">Tabs</h3>
		<Tabs.Root value="overview">
			<Tabs.List>
				<Tabs.Trigger value="overview">Overview</Tabs.Trigger>
				<Tabs.Trigger value="components">Components</Tabs.Trigger>
				<Tabs.Trigger value="tokens">Tokens</Tabs.Trigger>
			</Tabs.List>
			<Tabs.Content value="overview">
				<Card.Root>
					<Card.Content class="pt-6">
						<p class="text-sm text-muted-foreground">
							Bramble provides themes, components, and brand guidelines for all projects.
							Switch between themes to see how the same components adapt.
						</p>
					</Card.Content>
				</Card.Root>
			</Tabs.Content>
			<Tabs.Content value="components">
				<Card.Root>
					<Card.Content class="pt-6">
						<p class="text-sm text-muted-foreground">
							Built on shadcn-svelte (Bits UI). 60+ components available — buttons, cards,
							dialogs, forms, navigation, data display, and more.
						</p>
					</Card.Content>
				</Card.Root>
			</Tabs.Content>
			<Tabs.Content value="tokens">
				<Card.Root>
					<Card.Content class="pt-6">
						<p class="text-sm text-muted-foreground">
							Design tokens are CSS custom properties in OKLCH color space. Each theme
							defines ~40 variables covering colors, fonts, and radii.
						</p>
					</Card.Content>
				</Card.Root>
			</Tabs.Content>
		</Tabs.Root>
	</section>
</div>
