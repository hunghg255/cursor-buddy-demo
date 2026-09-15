import { CursorBuddy } from './components/cursor-buddy'
import './App.css'

const buddies = [
  { id: 'nik', name: 'Già Nik', detail: 'Luôn sẵn sàng chạy tiếp', color: '#e9e6fa' },
  { id: 'thinh', name: 'Thịnh', detail: 'Một chút bình yên', color: '#e5eedf' },
  { id: 'nemo', name: 'Nemo', detail: 'Chào bạn một cái nhé', color: '#e2ecf7' },
  { id: 'phuong', name: 'Phương', detail: 'Đang nghe bạn đây', color: '#f8e6dc' },
  { id: 'hung', name: 'Hùng', detail: 'Có mặt cùng cả hội', color: '#efe7d7' },
]

function App() {
  return (
    <main>
      <header className="topbar"><a href="#">cursor buddy<span>✳</span></a><span>Năm gương mặt, một hội bạn.</span></header>
      <section className="intro">
        <p className="eyebrow">MEET YOUR LITTLE CREW</p>
        <h1>Duckgang.<br /><span>Luôn nhìn theo bạn.</span></h1>
        <p>Di chuột để cả hội quay đầu. Bấm vào từng bạn để nhận một biểu cảm bất ngờ.</p>
      </section>
      <section className="buddies" aria-label="Năm cursor buddy từ ảnh của bạn">
        {buddies.map((buddy, index) => (
          <article className="buddy-card" key={buddy.id}>
            <div className="portrait" style={{ backgroundColor: buddy.color }}>
              <span className="number">0{index + 1}</span>
              <CursorBuddy directions={`/mascots/${buddy.id}-directions.webp`} reactions={`/mascots/${buddy.id}-reactions.webp`} size={220} label={buddy.name} className="mascot" />
              <span className="boop-hint">chạm nhẹ một cái ↗</span>
            </div>
            <div className="caption"><h2>{buddy.name}</h2><p>{buddy.detail}</p></div>
          </article>
        ))}
      </section>
      <footer><span>Ảnh thật → phiên bản chibi của bạn</span><span>Thử Tab + Enter hoặc Space để chào cả hội.</span></footer>
    </main>
  )
}

export default App
