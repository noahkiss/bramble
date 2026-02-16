export function load({ url }) {
	return {
		isEmbed: url.searchParams.has('embed')
	};
}
