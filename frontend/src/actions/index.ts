import { defineAction } from 'astro:actions';
import { z } from 'astro:schema';

export const server = {
  listCities: defineAction({
    accept: 'form',
    input: z.object({
      q: z.string(),
    }),
    handler: async ({ q }) => {
      const response = await fetch(`http://localhost:8000/forecast/search?q=${q}`);
      const data = await response.json();
      return data
    }
  })
}