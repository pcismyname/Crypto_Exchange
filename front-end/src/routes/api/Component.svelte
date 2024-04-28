<script>
    import yaml from "yaml";
    import isHotkey from "is-hotkey";
    import MessageView from "./Message.svelte";
    import { tick, createEventDispatcher } from "svelte";

    export let chat = ``;
    export let username = `user-1`;
    export let data = {};

    let message;
    let messages = [];
    let messageContainerRef;
    let dispatch = createEventDispatcher();

    function handleKeydown(event) {
        if (isHotkey("enter", event)) {
            handleSend();
        }
    }

    class Message {
        constructor({ text, username, timestamp }) {
            this.text = text;
            this.username = username;
            this.timestamp = timestamp || Date.now();
        }
    }

    function pushMessage(str) {
        const message = new Message({ text: str, username, isSender });
        messages = [...messages, message];
        updateChat();
    }

    function receiveMessage(str) {
        const message = new Message({ text: str, username, isSender });
        messages = [...messages, message];
        updateChat();
    }

    function parseMessages(str) {
        const parsed = yaml.parse(str) || [];

        if (parsed && parsed.messages) {
            data = parsed.data || data;
            return parsed.messages.map((message) => new Message(message));
        } else {
            return [];
        }
    }

    function updateChat() {
        chat = yaml.stringify({ messages, data });
    }

    function scrollToEnd() {
        if (messageContainerRef) {
            messageContainerRef.scrollTop = messageContainerRef.scrollHeight;
        }
    }

    async function handleSend() {
        if (message.trim()) {
            const newMessage = new Message({
                text: message,
                username,
                isSender: true,
            });
            messages = [...messages, newMessage];
            updateChat();

			const url = new URL("https://api.aiforthai.in.th/tagsuggestion");
        	url.searchParams.append('text', message);
			url.searchParams.append('numtag', 5);

			console.log(url)
        const options = {
            method: "GET",
            headers: {
				"Apikey": "RKUE2SFrXdaNkxanlt9XglWxJcKrmOlE",  // Assuming your API key is correct
            }
        };

            try {
                const response = await fetch(url, options);
                const data = await response.json();
				const tagString = data.tags.map(tag => tag.tag).join(', ');
                    const replyMessage = new Message({
                        text: 'ตอบ: ' + tagString,
                        username: "AI", // Assuming the AI's username
                        isSender: false,
                    });
                    messages = [...messages, replyMessage];
           
                message = "";
                await tick();
                scrollToEnd();
            } catch (error) {
                console.error("Error fetching data:", error);
                // Handle errors such as showing an error message to the user
            }
        }
    }

    $: console.log(data, messages, chat);
    $: messages = parseMessages(chat);
</script>

<div
    class="message-box rounded border border-radius mx-2 my-2 flex flex-col justify-between"
>
    <div class="rounded chat-header border-b px-4 py-1">
        <span>Chat with our AI assistant</span>
    </div>
    <div
        bind:this={messageContainerRef}
        class="flex-grow overflow-auto w-full h-full py-1"
    >
        <div
            style="min-height: 100%;"
            class="w-full chat-messages bg-primary overflow-auto flex flex-col justify-end"
        >
            {#each messages as message}
                <MessageView {...message} />
            {/each}
        </div>
    </div>

    <div class="chat-input h-8 flex mb-2">
        <span class="flex-grow mx-1">
            <input
                placeholder="type..."
                on:keydown={handleKeydown}
                bind:value={message}
                class="border rounded-lg bg-slate-200 px-2 w-full h-full"
            />
        </span>

        <button
            on:click={handleSend}
            class="rounded-lg border flex px-3 items-center mx-1 justify-center"
        >
            <span>send<span> <button> </button></span></span></button
        >
    </div>
</div>

<style>
    .message-box {
        width: 350px;
        height: 250px;
    }
</style>
