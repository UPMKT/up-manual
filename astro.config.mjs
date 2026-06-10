// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	integrations: [
		starlight({
			title: 'UP Manual',
			description: 'Manual operacional da UP Marketing & Comunicação — skills, squads, workflows e sistemas.',
			customCss: ['./src/styles/custom.css'],
			sidebar: [
				{
					label: 'Início',
					items: [{ label: 'Visão Geral', slug: 'home' }],
				},
				{
					label: 'Skills',
					items: [
						{ label: 'Catálogo Completo', slug: 'skills/catalog' },
						{
							label: 'GSD — Metodologia',
							items: [{ autogenerate: { directory: 'skills/gsd' } }],
						},
						{
							label: 'Upscale & GHL',
							items: [{ autogenerate: { directory: 'skills/upscale' } }],
						},
						{
							label: 'Marketing & Conteúdo',
							items: [{ autogenerate: { directory: 'skills/marketing' } }],
						},
						{
							label: 'Desenvolvimento',
							items: [{ autogenerate: { directory: 'skills/dev' } }],
						},
						{
							label: 'Ferramentas',
							items: [{ autogenerate: { directory: 'skills/tools' } }],
						},
					],
				},
				{
					label: 'Squads',
					items: [
						{ label: 'Todos os Squads', slug: 'squads/overview' },
						{
							label: 'Catálogo',
							items: [{ autogenerate: { directory: 'squads/catalog' } }],
						},
					],
				},
				{
					label: 'GHL & Upscale',
					items: [{ autogenerate: { directory: 'ghl' } }],
				},
				{
					label: 'GSD Metodologia',
					items: [{ autogenerate: { directory: 'gsd' } }],
				},
				{
					label: 'Referências',
					items: [{ autogenerate: { directory: 'reference' } }],
				},
			],
		}),
	],
});
