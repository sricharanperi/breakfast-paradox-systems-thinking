-- fenced divs -> boxed devices; bracketed spans -> evidence tags; chapter divider
local boxes = { exp="expcard", turning="turning", wrong="wrongbox", tradeoff="tradeoff", plain="plainwords", decision="decisionbox" }
local colors = { puzzle="cPuzzle", context="cContext", people="cPeople", process="cProcess", system="cSystem", cause="cCause", design="cDesign", test="cTest", look="cLook" }
function Div(el)
  for cls, env in pairs(boxes) do
    if el.classes:includes(cls) then
      local out = { pandoc.RawBlock("latex", "\\begin{" .. env .. "}") }
      for _, b in ipairs(el.content) do out[#out+1] = b end
      out[#out+1] = pandoc.RawBlock("latex", "\\end{" .. env .. "}")
      return out
    end
  end
  if el.classes:includes("quote") then
    local out = { pandoc.RawBlock("latex", "\\pullquote{") }
    for _, b in ipairs(el.content) do
      if b.t == "Para" or b.t == "Plain" then out[#out+1] = pandoc.Plain(b.content) else out[#out+1] = b end
    end
    out[#out+1] = pandoc.RawBlock("latex", "}")
    return out
  end
  if el.classes:includes("chapter") then
    local n = el.attributes["number"] or ""; local t = el.attributes["title"] or ""
    local col = colors[el.attributes["stage"] or "look"] or "cLook"
    local stage = el.attributes["label"] or ""
    local intro = pandoc.utils.stringify(el.content)
    local tex = "\\clearpage\\phantomsection\\addcontentsline{toc}{section}{" .. (n ~= "" and (n .. "  ") or "") .. t .. "}\n" ..
      "\\chapterpage{" .. n .. "}{" .. col .. "}{" .. t .. "}{" .. stage .. "}{" .. intro .. "}"
    return pandoc.RawBlock("latex", tex)
  end
end
function Span(el)
  local m = { c="cOk", s="cContext", k="cOpen", a="cLook", p="cDesign", sm="cCause", pl="cTest" }
  local names = { c="confirmed", s="single-sourced", k="candidate", a="assumed", p="projected", sm="simulated", pl="planned" }
  for cls, col in pairs(m) do
    if el.classes:includes(cls) then
      return pandoc.RawInline("latex", "\\evtag{" .. col .. "}{" .. names[cls] .. "}")
    end
  end
end
