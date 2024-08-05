import Image from "next/image";

export default function Header() {
  return (
    <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex">
      <div className="flex items-center gap-2">
        <Image
          src="/lora-chatbot-logo.png"
          alt="LoRa Chatbot Logo"
          width={24}
          height={24}
          priority
        />
        <span>LoRaWAN Chatbot</span>
      </div>
    </div>
  );
}
