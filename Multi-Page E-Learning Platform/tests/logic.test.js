const {
calculatePercentage,
determineGrade,
checkPassStatus,
getFeedback
} = require("../js/logic");

test("percentage calculation",()=>{
expect(calculatePercentage(8,10)).toBe(80);
});

test("grade calculation",()=>{
expect(determineGrade(85)).toBe("A");
});

test("pass fail logic",()=>{
expect(checkPassStatus(50)).toBe("Pass");
});

test("feedback for grade A",()=>{
expect(getFeedback("A")).toBe("Excellent performance!");
});