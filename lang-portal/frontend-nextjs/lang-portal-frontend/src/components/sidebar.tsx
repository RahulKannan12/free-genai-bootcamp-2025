import Link from "next/link";

const navItems = [
  { name: "Dashboard", path: "/dashboard" },
  { name: "Study Activities", path: "/study-activities" },
  { name: "Words", path: "/words" },
  { name: "Word Groups", path: "/groups" },
  { name: "Sessions", path: "/sessions" },
  { name: "Settings", path: "/settings" },
];

export default function Sidebar() {
  return (
    <div className="w-64 h-full bg-gray-800 text-white fixed">
      <div className="p-4 font-bold text-lg">LangPortal</div>
      <ul>
        {navItems.map((item) => (
          <li key={item.name} className="p-4 hover:bg-gray-700">
            <Link href={item.path}>{item.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}