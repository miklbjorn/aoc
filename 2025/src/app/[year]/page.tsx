import { App } from "@/components/App";

export default async function Home({params}: {params: Promise<{year: number}>}) {
  const {year} = await params;

  return (
        <App year={year} />
  );
}
