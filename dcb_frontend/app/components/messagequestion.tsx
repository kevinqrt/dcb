interface MessageQuestionProps {
    question: string;
}
const MessageQuestion: React.FC<MessageQuestionProps> = ({ question }) => {
    return (
    <>
        <div className="chat chat-end p-3">
        <div className="chat-bubble break-words bg-3 dark:bg-white">
            <p className="text-2 dark:text-4-dark">{question}</p>
        </div>
        </div>
    </>
    );
};
export default MessageQuestion;