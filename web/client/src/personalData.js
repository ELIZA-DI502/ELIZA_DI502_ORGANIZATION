// Warning before sending (KAN-26): the same patterns as the input check of the RAG service (D3),
// read from config/personal-data.json so that both use one definition.
import patterns from "../../../config/personal-data.json";

const email = new RegExp(patterns.email, "i");
const phone = new RegExp(patterns.phone, "gi");

export function findPersonalData(text) {
  const found = [];
  if (email.test(text)) found.push("an e-mail address");
  const phones = [...text.matchAll(phone)].filter(
    (m) => (m[0].match(/\d/g) ?? []).length >= patterns.phone_min_digits,
  );
  if (phones.length) found.push("a phone number");
  return found;
}
