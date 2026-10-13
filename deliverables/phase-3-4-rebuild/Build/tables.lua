-- Colour the header cells of every table (white bold on blue)
function Table(tbl)
  local head = tbl.head
  if head and head.rows then
    for _, row in ipairs(head.rows) do
      for _, cell in ipairs(row.cells) do
        local blocks = cell.contents
        if #blocks == 0 then
          blocks = { pandoc.Plain({}) }
        end
        local first = blocks[1]
        if first.t == "Plain" or first.t == "Para" then
          first.content:insert(1, pandoc.RawInline("latex", "\\cellcolor{pblue}\\color{white}\\bfseries "))
        end
        cell.contents = blocks
      end
    end
  end
  return tbl
end
