<script lang="ts">
	import Button from '$lib/components/Button.svelte';
	import * as Card from '$ui/card';
	import { Badge } from '$ui/badge';
	import * as Separator from '$ui/separator';
	import * as Tabs from '$ui/tabs';
	import { Input } from '$ui/input';
	import { Switch } from '$ui/switch';
	import { Checkbox } from '$ui/checkbox';
	import * as Select from '$ui/select';
	import * as Dialog from '$ui/dialog';
	import * as Tooltip from '$ui/tooltip';
	import Toggle from '$lib/components/Toggle.svelte';
	import { Progress } from '$ui/progress';
	import * as Accordion from '$ui/accordion';
	import * as Alert from '$ui/alert';
	import { Slider } from '$ui/slider';

	let switchChecked = $state(false);
	let checkboxChecked = $state(false);
	let progressValue = $state(45);
	let sliderValue = $state(35);
	let dialogOpen = $state(false);
	let selectValue = $state<string | undefined>(undefined);
	let toggleBold = $state(false);
	let toggleItalic = $state(false);
	let toggleUnderline = $state(false);
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
		<div class="grid grid-cols-2 gap-3 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6">
			{#each [
				{ name: 'Primary', bg: 'bg-primary', fg: 'text-primary-foreground' },
				{ name: 'Secondary', bg: 'bg-secondary', fg: 'text-secondary-foreground' },
				{ name: 'Accent', bg: 'bg-accent', fg: 'text-accent-foreground' },
				{ name: 'Muted', bg: 'bg-muted', fg: 'text-muted-foreground' },
				{ name: 'Destructive', bg: 'bg-destructive', fg: 'text-white' },
				{ name: 'Card', bg: 'bg-card', fg: 'text-card-foreground' },
				{ name: 'Success', bg: 'bg-success', fg: 'text-white' },
				{ name: 'Warning', bg: 'bg-warning', fg: 'text-white' },
				{ name: 'Background', bg: 'bg-background', fg: 'text-foreground' },
				{ name: 'Border', bg: 'bg-border', fg: 'text-foreground' },
				{ name: 'Ring', bg: 'bg-ring', fg: 'text-white' },
				{ name: 'Foreground', bg: 'bg-foreground', fg: 'text-background' }
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
			<p class="font-serif text-xl">Subheading — still the heading font, scaled down</p>
			<p class="text-lg">Body text uses the theme's body font. This paragraph demonstrates
				the default reading experience — line height, letter spacing, and overall rhythm.
				Good typography is invisible; you just read.</p>
			<p class="text-sm text-muted-foreground">
				Smaller body text for captions, descriptions, and secondary content.
			</p>
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
		<div class="flex flex-wrap items-center gap-3">
			<Button size="sm">Small</Button>
			<Button size="default">Default</Button>
			<Button size="lg">Large</Button>
			<Button disabled>Disabled</Button>
		</div>
		<div class="flex flex-wrap gap-3">
			<Button size="icon">
				<iconify-icon icon="solar:heart-bold" width="18"></iconify-icon>
			</Button>
			<Button variant="outline" size="icon">
				<iconify-icon icon="solar:settings-bold" width="18"></iconify-icon>
			</Button>
			<Button variant="ghost" size="icon">
				<iconify-icon icon="solar:bell-bold" width="18"></iconify-icon>
			</Button>
		</div>
	</section>

	<Separator.Root />

	<!-- Inputs -->
	<section class="space-y-4" data-section="inputs">
		<h3 class="text-xl font-semibold">Inputs</h3>
		<div class="grid gap-4 sm:grid-cols-2">
			<div class="space-y-2">
				<label for="input-default" class="text-sm font-medium">Default</label>
				<Input id="input-default" placeholder="Type something..." />
			</div>
			<div class="space-y-2">
				<label for="input-disabled" class="text-sm font-medium">Disabled</label>
				<Input id="input-disabled" placeholder="Can't touch this" disabled />
			</div>
			<div class="space-y-2">
				<label for="input-email" class="text-sm font-medium">Email</label>
				<Input id="input-email" type="email" placeholder="penny@bramble.dev" />
			</div>
			<div class="space-y-2">
				<label for="input-search" class="text-sm font-medium">Search</label>
				<Input id="input-search" type="search" placeholder="Search components..." />
			</div>
		</div>
	</section>

	<Separator.Root />

	<!-- Select -->
	<section class="space-y-4" data-section="select">
		<h3 class="text-xl font-semibold">Select</h3>
		<div class="max-w-xs">
			<Select.Root type="single" bind:value={selectValue}>
				<Select.Trigger>
					{selectValue ?? 'Choose a project...'}
				</Select.Trigger>
				<Select.Content align="start" strategy="fixed">
					<Select.Item value="tinyledger">TinyLedger</Select.Item>
					<Select.Item value="recall">Recall</Select.Item>
					<Select.Item value="storyteller">Storyteller</Select.Item>
					<Select.Item value="bramble">Bramble</Select.Item>
				</Select.Content>
			</Select.Root>
		</div>
	</section>

	<Separator.Root />

	<!-- Switches & Checkboxes -->
	<section class="space-y-4" data-section="toggles">
		<h3 class="text-xl font-semibold">Switches &amp; Checkboxes</h3>
		<div class="flex flex-wrap gap-8">
			<div class="flex items-center gap-3">
				<Switch bind:checked={switchChecked} id="switch-demo" />
				<label for="switch-demo" class="inline-block w-8 text-sm font-medium">
					{switchChecked ? 'On' : 'Off'}
				</label>
			</div>
			<div class="flex items-center gap-3">
				<Checkbox bind:checked={checkboxChecked} id="checkbox-demo" />
				<label for="checkbox-demo" class="text-sm font-medium">
					Accept terms
				</label>
			</div>
			<div class="flex items-center gap-3">
				<Checkbox checked={true} disabled id="checkbox-disabled" />
				<label for="checkbox-disabled" class="text-sm font-medium text-muted-foreground">
					Checked (disabled)
				</label>
			</div>
		</div>
	</section>

	<Separator.Root />

	<!-- Toggle -->
	<section class="space-y-4" data-section="toggle">
		<h3 class="text-xl font-semibold">Toggle</h3>
		<div class="flex flex-wrap gap-2">
			<Toggle bind:pressed={toggleBold} aria-label="Toggle bold">
				<iconify-icon icon="solar:text-bold-bold" width="18"></iconify-icon>
			</Toggle>
			<Toggle bind:pressed={toggleItalic} aria-label="Toggle italic">
				<iconify-icon icon="solar:text-italic-bold" width="18"></iconify-icon>
			</Toggle>
			<Toggle bind:pressed={toggleUnderline} aria-label="Toggle underline">
				<iconify-icon icon="solar:text-underline-bold" width="18"></iconify-icon>
			</Toggle>
		</div>
		<p
			class="text-sm text-muted-foreground"
			class:font-bold={toggleBold}
			class:italic={toggleItalic}
			class:underline={toggleUnderline}
		>
			The quick brown fox jumps over the lazy dog.
		</p>
	</section>

	<Separator.Root />

	<!-- Slider & Progress -->
	<section class="space-y-6" data-section="range">
		<h3 class="text-xl font-semibold">Slider &amp; Progress</h3>
		<div class="space-y-4 max-w-md">
			<div class="space-y-2">
				<div class="flex items-center justify-between">
					<span class="text-sm font-medium">Slider</span>
					<span class="text-sm text-muted-foreground">{sliderValue}</span>
				</div>
				<Slider type="single" bind:value={sliderValue} max={100} step={1} />
			</div>
			<div class="space-y-2">
				<div class="flex items-center justify-between">
					<span class="text-sm font-medium">Progress</span>
					<span class="text-sm text-muted-foreground">{progressValue}%</span>
				</div>
				<Progress value={progressValue} />
			</div>
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

	<!-- Alerts -->
	<section class="space-y-4" data-section="alerts">
		<h3 class="text-xl font-semibold">Alerts</h3>
		<div class="space-y-3">
			<Alert.Root data-variant="info">
				<iconify-icon icon="solar:info-circle-bold" width="16" class="mt-0.5"></iconify-icon>
				<Alert.Title>Heads up</Alert.Title>
				<Alert.Description>
					Components adapt to the active theme automatically via CSS custom properties.
				</Alert.Description>
			</Alert.Root>
			<Alert.Root data-variant="success">
				<iconify-icon icon="solar:check-circle-bold" width="16" class="mt-0.5"></iconify-icon>
				<Alert.Title>Success</Alert.Title>
				<Alert.Description>
					Your changes have been saved and deployed.
				</Alert.Description>
			</Alert.Root>
			<Alert.Root data-variant="warning">
				<iconify-icon icon="solar:shield-warning-bold" width="16" class="mt-0.5"></iconify-icon>
				<Alert.Title>Warning</Alert.Title>
				<Alert.Description>
					API rate limit is at 80%. Consider upgrading your plan.
				</Alert.Description>
			</Alert.Root>
			<Alert.Root data-variant="error">
				<iconify-icon icon="solar:danger-triangle-bold" width="16" class="mt-0.5"></iconify-icon>
				<Alert.Title>Error</Alert.Title>
				<Alert.Description>
					Something went wrong. Check the console for details.
				</Alert.Description>
			</Alert.Root>
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
					<Card.Title>Recall</Card.Title>
					<Card.Description>Claude conversation search &amp; memory</Card.Description>
				</Card.Header>
				<Card.Content>
					<p class="text-sm text-muted-foreground">
						Search and resurface past conversations. Penny's explorer look — backpack and compass.
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

	<!-- Dialog -->
	<section class="space-y-4" data-section="dialog">
		<h3 class="text-xl font-semibold">Dialog</h3>
		<Dialog.Root bind:open={dialogOpen}>
			<Dialog.Trigger>
				{#snippet child({ props })}
					<Button variant="outline" {...props}>Open Dialog</Button>
				{/snippet}
			</Dialog.Trigger>
			<Dialog.Content>
				<Dialog.Header>
					<Dialog.Title>Design tokens</Dialog.Title>
					<Dialog.Description>
						Each theme defines ~40 CSS custom properties in OKLCH color space covering
						colors, fonts, and border radii.
					</Dialog.Description>
				</Dialog.Header>
				<div class="space-y-3 py-4">
					<div class="flex items-center justify-between">
						<span class="text-sm font-medium">Primary</span>
						<div class="flex items-center gap-2">
							<div class="h-4 w-4 rounded-full bg-primary"></div>
							<span class="font-mono text-xs text-muted-foreground">--primary</span>
						</div>
					</div>
					<div class="flex items-center justify-between">
						<span class="text-sm font-medium">Accent</span>
						<div class="flex items-center gap-2">
							<div class="h-4 w-4 rounded-full bg-accent"></div>
							<span class="font-mono text-xs text-muted-foreground">--accent</span>
						</div>
					</div>
					<div class="flex items-center justify-between">
						<span class="text-sm font-medium">Destructive</span>
						<div class="flex items-center gap-2">
							<div class="h-4 w-4 rounded-full bg-destructive"></div>
							<span class="font-mono text-xs text-muted-foreground">--destructive</span>
						</div>
					</div>
				</div>
				<Dialog.Footer>
					<Button variant="outline" onclick={() => (dialogOpen = false)}>Close</Button>
				</Dialog.Footer>
			</Dialog.Content>
		</Dialog.Root>
	</section>

	<Separator.Root />

	<!-- Tooltip -->
	<section class="space-y-4" data-section="tooltip">
		<h3 class="text-xl font-semibold">Tooltip</h3>
		<div class="flex flex-wrap gap-3">
			<Tooltip.Provider>
				<Tooltip.Root>
					<Tooltip.Trigger>
						{#snippet child({ props })}
							<Button variant="outline" {...props}>Hover me</Button>
						{/snippet}
					</Tooltip.Trigger>
					<Tooltip.Content>
						<p>Tooltip content goes here</p>
					</Tooltip.Content>
				</Tooltip.Root>
			</Tooltip.Provider>
			<Tooltip.Provider>
				<Tooltip.Root>
					<Tooltip.Trigger>
						{#snippet child({ props })}
							<Button variant="ghost" size="icon" {...props}>
								<iconify-icon icon="solar:question-circle-bold" width="18"></iconify-icon>
							</Button>
						{/snippet}
					</Tooltip.Trigger>
					<Tooltip.Content>
						<p>Need help?</p>
					</Tooltip.Content>
				</Tooltip.Root>
			</Tooltip.Provider>
		</div>
	</section>

	<Separator.Root />

	<!-- Accordion -->
	<section class="space-y-4" data-section="accordion">
		<h3 class="text-xl font-semibold">Accordion</h3>
		<Accordion.Root type="single" class="max-w-lg">
			<Accordion.Item value="themes">
				<Accordion.Trigger>How do themes work?</Accordion.Trigger>
				<Accordion.Content>
					Themes are CSS custom properties defined in OKLCH color space. Switching themes
					swaps the property values — components don't need to know which theme is active.
				</Accordion.Content>
			</Accordion.Item>
			<Accordion.Item value="components">
				<Accordion.Trigger>What component library is this?</Accordion.Trigger>
				<Accordion.Content>
					Built on shadcn-svelte, which wraps Bits UI primitives with styled defaults.
					Tailwind handles styling inside components; CSS custom properties handle theming.
				</Accordion.Content>
			</Accordion.Item>
			<Accordion.Item value="penny">
				<Accordion.Trigger>Who is Penny?</Accordion.Trigger>
				<Accordion.Content>
					Penny is the brand mascot — a Cavalier King Charles Spaniel rendered in a
					storybook watercolor style. She has different looks for different projects.
				</Accordion.Content>
			</Accordion.Item>
		</Accordion.Root>
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
					<Card.Content class="space-y-3 py-4">
						<p class="text-sm">
							Bramble is a personal design system that provides themes, components, and brand guidelines.
							Switch themes above to see every component on this page adapt instantly.
						</p>
						<div class="flex flex-wrap gap-2">
							<Badge>Svelte 5</Badge>
							<Badge variant="secondary">Tailwind 4</Badge>
							<Badge variant="outline">OKLCH</Badge>
						</div>
					</Card.Content>
				</Card.Root>
			</Tabs.Content>
			<Tabs.Content value="components">
				<Card.Root>
					<Card.Content class="py-4">
						<div class="grid gap-3 sm:grid-cols-3">
							{#each [
								{ label: 'Inputs', count: 4, icon: 'solar:text-field-bold' },
								{ label: 'Feedback', count: 5, icon: 'solar:chat-round-dots-bold' },
								{ label: 'Layout', count: 4, icon: 'solar:widget-bold' }
							] as group}
								<div class="flex items-center gap-3 rounded-md border border-border p-3">
									<iconify-icon icon={group.icon} width="20" class="text-primary"></iconify-icon>
									<div>
										<p class="text-sm font-medium">{group.label}</p>
										<p class="text-xs text-muted-foreground">{group.count} components</p>
									</div>
								</div>
							{/each}
						</div>
					</Card.Content>
				</Card.Root>
			</Tabs.Content>
			<Tabs.Content value="tokens">
				<Card.Root>
					<Card.Content class="py-4">
						<div class="space-y-2">
							{#each [
								{ token: '--primary', preview: 'bg-primary' },
								{ token: '--accent', preview: 'bg-accent' },
								{ token: '--destructive', preview: 'bg-destructive' },
								{ token: '--success', preview: 'bg-success' },
								{ token: '--warning', preview: 'bg-warning' }
							] as row}
								<div class="flex items-center gap-3">
									<div class="h-4 w-4 rounded-full {row.preview} shrink-0"></div>
									<code class="text-xs font-mono text-muted-foreground">{row.token}</code>
								</div>
							{/each}
						</div>
					</Card.Content>
				</Card.Root>
			</Tabs.Content>
		</Tabs.Root>
	</section>
</div>
