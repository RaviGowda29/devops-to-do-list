export default async function Page() {
  const res = await fetch("http://backend:8000/tasks", { cache: "no-store" });
  const data = await res.json();

  return (
    <main style={{ padding: "2rem" }}>
      <h1>ToDo List</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}
